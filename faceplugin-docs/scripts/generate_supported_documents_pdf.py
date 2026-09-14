"""Generate FacePlugin ID Document Recognition — Supported Documents PDF."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    FrameBreak,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / ".gitbook" / "assets"
DATA = ASSETS / "_doc_types_parsed.json"
RELEASE_NOTES = ASSETS / "_release_notes_docs.json"
OUT = ASSETS / "faceplugin-supported-documents.pdf"

# Brand — deep teal / charcoal (avoid purple/cream defaults)
C_BG = colors.HexColor("#0B1F2A")
C_ACCENT = colors.HexColor("#1FA8A0")
C_ACCENT2 = colors.HexColor("#F0B429")
C_TEXT = colors.HexColor("#12212B")
C_MUTED = colors.HexColor("#5A6B75")
C_LINE = colors.HexColor("#D7E0E6")
C_CARD = colors.HexColor("#F4F8F9")
C_WHITE = colors.white


def load():
    meta = json.loads(DATA.read_text(encoding="utf-8"))
    # Optional extras from release notes are only merged when catalog is not already full
    if meta.get("full_list"):
        meta["release_new_docs"] = []
        meta["release_results"] = []
        meta["release_latest"] = None
        return meta
    rn = {}
    if RELEASE_NOTES.exists():
        rn = json.loads(RELEASE_NOTES.read_text(encoding="utf-8"))
    latest = rn.get("latest") or {}
    if latest.get("db_documents"):
        meta["database_documents"] = latest["db_documents"]
    if latest.get("db_countries"):
        meta["database_countries"] = latest["db_countries"]
    meta["release_latest"] = latest.get("version")
    meta["release_new_docs"] = rn.get("new_docs") or []
    meta["release_results"] = rn.get("results") or []
    docs_by = {k: list(v) for k, v in (meta.get("docs_by_country") or {}).items()}
    country_counts = dict(meta.get("country_counts") or {})
    for item in meta["release_new_docs"]:
        name = item["name"]
        country, _title = split_country_title(name)
        if country == "(Other)":
            bucket = docs_by.setdefault("International / other", [])
            if name not in bucket:
                bucket.append(name)
            country_counts["International / other"] = max(
                country_counts.get("International / other", 0), len(bucket)
            )
            continue
        if country not in country_counts:
            country_counts[country] = country_counts.get(country, 0) + 1
        bucket = docs_by.setdefault(country, [])
        if name not in bucket:
            bucket.append(name)
    meta["docs_by_country"] = {k: sorted(set(v), key=str.lower) for k, v in docs_by.items()}
    meta["country_counts"] = country_counts
    return meta


def split_country_title(name: str) -> tuple[str, str]:
    import re

    m = re.search(
        r"\b(Passport|ePassport|ID Card|Id Card|Identity Card|Driving License|Driver.?s License|\bDL\b|"
        r"Visa|eVisa|Residence Permit|Residence Card|Resident Card|Work Permit|Refugee|"
        r"Registration Certificate|Health Insurance|Social Security|Diplomatic|Consular|"
        r"Border Crossing|Business Travel|Immigration|Citizenship|Crew|Laissez|Proof of Age|"
        r"Police|Lawyer|Marine|Tax Card|Voter|Permanent Resident|Alien|Foreigner|Temporary|"
        r"Seaman|Seafarer|Green Card|mDL|eDL|National ID|Travel Document|Certificate|"
        r"Birth Certificate|Armed Forces|Digital ID|Digital Certificate|Forces ID|AES ID|"
        r"Card|License|Permit|Book)\b",
        name,
        re.I,
    )
    if not m:
        return ("(Other)", name)
    country = name[: m.start()].strip(" -") or "(Other)"
    return (country, name)


def styles():
    ss = getSampleStyleSheet()
    ss.add(
        ParagraphStyle(
            "CoverBrand",
            fontName="Helvetica-Bold",
            fontSize=28,
            textColor=C_WHITE,
            alignment=TA_LEFT,
            leading=34,
            spaceAfter=8,
        )
    )
    ss.add(
        ParagraphStyle(
            "CoverTitle",
            fontName="Helvetica-Bold",
            fontSize=22,
            textColor=C_WHITE,
            alignment=TA_LEFT,
            leading=28,
            spaceBefore=18,
            spaceAfter=10,
        )
    )
    ss.add(
        ParagraphStyle(
            "CoverSub",
            fontName="Helvetica",
            fontSize=11,
            textColor=colors.HexColor("#B7C9D2"),
            alignment=TA_LEFT,
            leading=16,
            spaceAfter=6,
        )
    )
    ss.add(
        ParagraphStyle(
            "H1",
            fontName="Helvetica-Bold",
            fontSize=18,
            textColor=C_TEXT,
            spaceBefore=0,
            spaceAfter=10,
            leading=22,
        )
    )
    ss.add(
        ParagraphStyle(
            "H2",
            fontName="Helvetica-Bold",
            fontSize=12,
            textColor=C_TEXT,
            spaceBefore=12,
            spaceAfter=6,
            leading=15,
        )
    )
    ss.add(
        ParagraphStyle(
            "Body",
            fontName="Helvetica",
            fontSize=9.5,
            textColor=C_TEXT,
            leading=13,
            spaceAfter=6,
        )
    )
    ss.add(
        ParagraphStyle(
            "Muted",
            fontName="Helvetica",
            fontSize=8.5,
            textColor=C_MUTED,
            leading=11,
            spaceAfter=4,
        )
    )
    ss.add(
        ParagraphStyle(
            "StatNum",
            fontName="Helvetica-Bold",
            fontSize=22,
            textColor=C_ACCENT,
            alignment=TA_CENTER,
            leading=26,
        )
    )
    ss.add(
        ParagraphStyle(
            "StatLabel",
            fontName="Helvetica",
            fontSize=8,
            textColor=C_MUTED,
            alignment=TA_CENTER,
            leading=10,
        )
    )
    ss.add(
        ParagraphStyle(
            "CountryHead",
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=C_TEXT,
            spaceBefore=8,
            spaceAfter=3,
            leading=12,
        )
    )
    ss.add(
        ParagraphStyle(
            "DocItem",
            fontName="Helvetica",
            fontSize=7.5,
            textColor=C_TEXT,
            leading=10,
            leftIndent=2,
        )
    )
    ss.add(
        ParagraphStyle(
            "Footer",
            fontName="Helvetica",
            fontSize=7.5,
            textColor=C_MUTED,
            alignment=TA_CENTER,
        )
    )
    ss.add(
        ParagraphStyle(
            "CatItem",
            fontName="Helvetica",
            fontSize=8.5,
            textColor=C_TEXT,
            leading=11,
            leftIndent=6,
            bulletIndent=0,
        )
    )
    ss.add(
        ParagraphStyle(
            "CardTitle",
            fontName="Helvetica-Bold",
            fontSize=8,
            textColor=C_TEXT,
            leading=10,
            alignment=TA_LEFT,
        )
    )
    ss.add(
        ParagraphStyle(
            "CardMeta",
            fontName="Helvetica",
            fontSize=7,
            textColor=C_MUTED,
            leading=9,
            alignment=TA_LEFT,
        )
    )
    return ss


def draw_cover(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(C_BG)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    # accent bar
    canvas.setFillColor(C_ACCENT)
    canvas.rect(0, 0, 8 * mm, h, fill=1, stroke=0)
    # top accent line
    canvas.setStrokeColor(C_ACCENT)
    canvas.setLineWidth(1.2)
    canvas.line(18 * mm, h - 28 * mm, w - 18 * mm, h - 28 * mm)
    # bottom band
    canvas.setFillColor(colors.HexColor("#07151C"))
    canvas.rect(0, 0, w, 22 * mm, fill=1, stroke=0)
    canvas.setFillColor(C_ACCENT2)
    canvas.rect(8 * mm, 22 * mm - 2, w - 8 * mm, 2, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#8FA3AE"))
    canvas.setFont("Helvetica", 8)
    canvas.drawString(18 * mm, 10 * mm, "faceplugin.com  ·  doc.faceplugin.com  ·  Confidential customer catalog")
    canvas.restoreState()


def draw_inner(canvas, doc):
    canvas.saveState()
    w, h = A4
    # header rule
    canvas.setStrokeColor(C_LINE)
    canvas.setLineWidth(0.6)
    canvas.line(16 * mm, h - 12 * mm, w - 16 * mm, h - 12 * mm)
    canvas.setFillColor(C_ACCENT)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(16 * mm, h - 9 * mm, "FACEPLUGIN")
    canvas.setFillColor(C_MUTED)
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(w - 16 * mm, h - 9 * mm, "ID Document Recognition — Supported Documents")
    # footer
    canvas.setStrokeColor(C_LINE)
    canvas.line(16 * mm, 12 * mm, w - 16 * mm, 12 * mm)
    canvas.setFillColor(C_MUTED)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(16 * mm, 7 * mm, f"Updated {date.today().isoformat()}")
    canvas.drawRightString(w - 16 * mm, 7 * mm, f"{doc.page}")
    canvas.restoreState()


def stat_cards(meta, S):
    docs = f"{meta['database_documents']:,}"
    countries = str(meta["database_countries"])
    types = "30+"
    data = [
        [
            Paragraph(docs, S["StatNum"]),
            Paragraph(countries, S["StatNum"]),
            Paragraph(types, S["StatNum"]),
        ],
        [
            Paragraph("Document templates", S["StatLabel"]),
            Paragraph("Countries & territories", S["StatLabel"]),
            Paragraph("Document type families", S["StatLabel"]),
        ],
    ]
    t = Table(data, colWidths=[55 * mm, 55 * mm, 55 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), C_CARD),
                ("BOX", (0, 0), (-1, -1), 0.5, C_LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, C_LINE),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return t


def build():
    meta = load()
    S = styles()
    doc = BaseDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=18 * mm,
        bottomMargin=16 * mm,
        title="Faceplugin Supported Documents",
        author="Faceplugin",
    )
    frame_cover = Frame(18 * mm, 30 * mm, A4[0] - 36 * mm, A4[1] - 60 * mm, id="cover")
    frame_inner = Frame(16 * mm, 16 * mm, A4[0] - 32 * mm, A4[1] - 34 * mm, id="inner")
    # 2-col for catalog
    gap = 6 * mm
    col_w = (A4[0] - 32 * mm - gap) / 2
    frame_l = Frame(16 * mm, 16 * mm, col_w, A4[1] - 34 * mm, id="left")
    frame_r = Frame(16 * mm + col_w + gap, 16 * mm, col_w, A4[1] - 34 * mm, id="right")

    doc.addPageTemplates(
        [
            PageTemplate(id="cover", frames=[frame_cover], onPage=draw_cover),
            PageTemplate(id="inner", frames=[frame_inner], onPage=draw_inner),
            PageTemplate(id="twocol", frames=[frame_l, frame_r], onPage=draw_inner),
        ]
    )

    story = []

    # —— Cover ——
    story.append(Paragraph("FACEPLUGIN", S["CoverBrand"]))
    story.append(Paragraph("ID Document Recognition SDK", S["CoverSub"]))
    story.append(Paragraph("Supported Document Types", S["CoverTitle"]))
    story.append(
        Paragraph(
            "Customer catalog of identity document templates handled by the "
            "Faceplugin Document Reader engine — passports, national IDs, driver licenses, "
            "visas, residence permits, and specialized credentials worldwide.",
            S["CoverSub"],
        )
    )
    story.append(Spacer(1, 14 * mm))
    story.append(
        Paragraph(
            f"<font color='#1FA8A0'><b>{meta['database_documents']:,}</b></font>  templates &nbsp;&nbsp;·&nbsp;&nbsp; "
            f"<font color='#1FA8A0'><b>{meta['database_countries']}</b></font>  countries &amp; territories",
            S["CoverSub"],
        )
    )
    story.append(Spacer(1, 8 * mm))
    story.append(
        Paragraph(
            "Automatic document-type classification · OCR / MRZ / barcode · "
            "Optional authenticity (document liveness) when licensed",
            S["CoverSub"],
        )
    )
    story.append(NextPageTemplate("inner"))
    story.append(PageBreak())

    # —— Overview ——
    story.append(Paragraph("Overview", S["H1"]))
    story.append(
        Paragraph(
            "Faceplugin ID Document Recognition identifies the issuing country and document series, "
            "then reads the visual zone, MRZ, and barcodes. The same engine powers Android, iOS, "
            "Flutter, React Native, Ionic, Windows, and Linux / Docker (HTTP port <b>8082</b>).",
            S["Body"],
        )
    )
    story.append(stat_cards(meta, S))
    story.append(Spacer(1, 4 * mm))
    story.append(
        Paragraph(
            f"This catalog lists all <b>{meta['database_documents']:,}</b> document templates across "
            f"<b>{meta['database_countries']}</b> countries and territories.",
            S["Muted"],
        )
    )

    story.append(Paragraph("Document type families", S["H1"]))
    story.append(
        Paragraph(
            "Templates are grouped by how customers use them in KYC / eKYC flows — not by internal IDs.",
            S["Body"],
        )
    )

    cat_rows = []
    for title, items in meta["categories"]:
        bullets = "<br/>".join(f"• {x}" for x in items)
        cat_rows.append(
            [
                Paragraph(f"<b>{title}</b>", S["Body"]),
                Paragraph(bullets, S["CatItem"]),
            ]
        )
    cat_table = Table(cat_rows, colWidths=[42 * mm, 123 * mm])
    cat_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), C_CARD),
                ("BOX", (0, 0), (-1, -1), 0.5, C_LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, C_LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(cat_table)

    story.append(Paragraph("Most common template families", S["H2"]))
    top = []
    seen = set()
    for name, cnt in meta["type_hits"]:
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)
        top.append((name, cnt))
        if len(top) >= 12:
            break
    top_data = [[Paragraph("<b>Family</b>", S["Muted"]), Paragraph("<b>Approx. template hits*</b>", S["Muted"])]]
    for name, cnt in top:
        top_data.append([Paragraph(name, S["Body"]), Paragraph(str(cnt), S["Body"])])
    top_t = Table(top_data, colWidths=[120 * mm, 45 * mm])
    top_t.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, 0), 1, C_ACCENT),
                ("LINEBELOW", (0, 1), (-1, -2), 0.3, C_LINE),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(top_t)
    story.append(
        Paragraph(
            "*Counts include front/back/page variants where present in the catalog.",
            S["Muted"],
        )
    )

    story.append(PageBreak())
    story.append(Paragraph("Countries & territories index", S["H1"]))
    story.append(
        Paragraph(
            "Template count per issuing country or territory. Sort is alphabetical.",
            S["Body"],
        )
    )

    countries = sorted(meta["country_counts"].items(), key=lambda x: x[0].lower())
    cols = 3
    chunk = []
    for i in range(0, len(countries), cols):
        row = []
        for j in range(cols):
            if i + j < len(countries):
                name, n = countries[i + j]
                row.append(Paragraph(f"<b>{name}</b><br/><font color='#5A6B75' size='8'>{n} templates</font>", S["Body"]))
            else:
                row.append("")
        chunk.append(row)
    idx = Table(chunk, colWidths=[55 * mm, 55 * mm, 55 * mm])
    idx.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), C_WHITE),
                ("BOX", (0, 0), (-1, -1), 0.4, C_LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.3, C_LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [C_WHITE, C_CARD]),
            ]
        )
    )
    story.append(idx)

    # —— Detailed catalog ——
    story.append(NextPageTemplate("twocol"))
    story.append(PageBreak())
    story.append(Paragraph("Document catalog by country", S["H1"]))
    story.append(
        Paragraph(
            "Full document list by issuing country or territory. "
            "Side B / page variants appear as separate entries when present.",
            S["Muted"],
        )
    )

    ordered = sorted(meta["country_counts"].keys(), key=lambda s: s.lower())
    listed = 0
    for ctry in ordered:
        n = meta["country_counts"][ctry]
        titles = list(meta["docs_by_country"].get(ctry) or [])
        story.append(Paragraph(f"{ctry}  <font color='#5A6B75'>({n})</font>", S["CountryHead"]))
        if not titles:
            story.append(Paragraph(f"<font color='#5A6B75'>· {n} templates</font>", S["DocItem"]))
            story.append(Spacer(1, 2 * mm))
            continue
        # Full list — every database row (including Side B / page variants)
        chunk_size = 120
        for i in range(0, len(titles), chunk_size):
            chunk = titles[i : i + chunk_size]
            body = "<br/>".join(f"· {escape(x)}" for x in chunk)
            story.append(Paragraph(body, S["DocItem"]))
            listed += len(chunk)
        story.append(Spacer(1, 2 * mm))
    print("Listed document titles:", listed)

    story.append(NextPageTemplate("inner"))
    story.append(PageBreak())
    story.append(Paragraph("Notes & contact", S["H1"]))
    story.append(
        Paragraph(
            "• This PDF is the <b>Faceplugin</b> customer catalog for ID Document Recognition.<br/>"
            "• Coverage grows over time; contact us if you need confirmation for a specific series.<br/>"
            "• RFID / NFC chip reading and multi-spectral authenticity depend on platform and license.<br/>"
            "• Document authenticity without OCR is also available as the dedicated <b>ID Document Liveness</b> Linux product (port 8086).",
            S["Body"],
        )
    )
    story.append(Spacer(1, 4 * mm))
    story.append(
        Paragraph(
            "<b>License &amp; support</b><br/>"
            "info@faceplugin.com · https://doc.faceplugin.com · https://faceplugin.com",
            S["Body"],
        )
    )

    doc.build(story)
    print("Wrote", OUT, "size", OUT.stat().st_size)


def escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def re_sub_side(t: str) -> str:
    import re

    t = re.sub(r"\s+Side B(?:\s*#?\d+)?$", "", t, flags=re.I)
    t = re.sub(r"\s+Side$", "", t, flags=re.I)
    return t.strip()


if __name__ == "__main__":
    build()
