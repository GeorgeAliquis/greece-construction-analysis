# Greece Construction Activity | 2025

**Documentation:** 🇬🇧 **English** | 🇬🇷 [Ελληνικά](README.el.md)

---

## Overview
An interactive **Power BI dashboard** exploring new building activity across Greece in **2025**, using publicly available data from the **Hellenic Statistical Authority (ELSTAT)**.

The project transforms ELSTAT's published Excel tables into a clean, analysis-ready dataset and makes it possible to compare construction activity at two geographic levels: **regions** and **regional units**. The current report covers **January–December 2025**; expanding it into a multi-year, monthly time-series analysis is the next major goal.

---

## Table of Contents

- [Overview](#overview)
- [Dashboard Previews](#dashboard-previews)
- [Project Overview](#project-overview)
- [Key Findings](#key-findings)
  - [Regions](#regions)
  - [Regional Units](#regional-units)
- [Dashboard Features](#dashboard-features)
  - [Visualizations and Interactive Controls](#visualizations-and-interactive-controls)
  - [Dynamic Chart Labels](#dynamic-chart-labels)
- [Data Source](#data-source)
- [Data Cleaning and Preparation](#data-cleaning-and-preparation)
  - [Original vs. Cleaned Data](#original-vs-cleaned-data)
- [Tools and Techniques](#tools-and-techniques)
- [Project Structure](#project-structure)
- [Roadmap / TODO](#roadmap--todo)
- [Project Status](#project-status)

---

## Dashboard previews

The dashboard is presented in Greek to preserve the names of administrative areas and make the analysis accessible to a Greek-speaking audience. **Click either preview to view it at full size.**

<table>
  <tr>
    <th align="center" width="50%">Regions</th>
    <th align="center" width="50%">Regional units</th>
  </tr>
  <tr>
    <td align="center" valign="middle">
      <a href="assets/greece-construction-analysis-regions-dashboard-v1.png">
        <img src="assets/greece-construction-analysis-regions-dashboard-v1.png" alt="Power BI construction dashboard displaying Greek regions" width="100%" />
      </a>
    </td>
    <td align="center" valign="middle">
      <a href="assets/greece-construction-analysis-regional_units-dashboard-v1.png">
        <img src="assets/greece-construction-analysis-regional_units-dashboard-v1.png" alt="Power BI construction dashboard displaying Greek regional units" width="100%" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center"><sub>Aggregated comparison across Greece's regions</sub></td>
    <td align="center"><sub>More detailed comparison across regional units</sub></td>
  </tr>
</table>

---

## Project overview

The analysis examines four measures of newly built properties:

| Indicator | Greece, 2025 |
| --- | ---: |
| **Buildings** | **11,650** |
| **Storeys** | **24,292** |
| **Total building volume** | **20,608,577 m³** |
| **Total building surface area** | **4,731,479 m²** |

These figures describe the **2025 reporting period**, not a monthly trend. Geographic comparisons use the appropriate administrative level to avoid counting the same activity twice through both region and regional-unit rows.

---

## Key findings

**Attica leads all four indicators** at the regional level, accounting for approximately **18.3% of new buildings**, **27.9% of total surface area**, **28.1% of building volume**, and **28.2% of storeys** nationwide. Among regional units, **East Attica** leads in buildings and storeys, while **Thessaloniki** leads in surface area and volume.

The following rankings show the three highest and lowest absolute values for each indicator in 2025. These are **totals**, not population-adjusted construction rates.

### Regions

| Indicator | Top 3 (highest first) | Bottom 3 (lowest first) |
| --- | --- | --- |
| **Buildings** | 1. Attica (**2,134**)<br>2. Crete (**1,509**)<br>3. Central Macedonia (**1,363**) | 1. Western Macedonia (**110**)<br>2. North Aegean (**283**)<br>3. Epirus (**446**) |
| **Surface area (m²)** | 1. Attica (**1,320,364**)<br>2. Central Macedonia (**698,026**)<br>3. Crete (**446,073**) | 1. Western Macedonia (**49,964**)<br>2. North Aegean (**65,194**)<br>3. Epirus (**182,077**) |
| **Building volume (m³)** | 1. Attica (**5,781,828**)<br>2. Central Macedonia (**3,553,809**)<br>3. Crete (**1,673,408**) | 1. North Aegean (**235,244**)<br>2. Western Macedonia (**291,672**)<br>3. Epirus (**695,689**) |
| **Storeys** | 1. Attica (**6,851**)<br>2. Central Macedonia (**2,886**)<br>3. Crete (**2,656**) | 1. Western Macedonia (**170**)<br>2. North Aegean (**462**)<br>3. Epirus (**822**) |

### Regional units

| Indicator | Top 3 (highest first) | Bottom 3 (lowest first) |
| --- | --- | --- |
| **Buildings** | 1. East Attica (**793**)<br>2. Thessaloniki (**636**)<br>3. Chania (**520**) | 1. Ithaca (**11**)<br>2. Evrytania (**11**)<br>3. Ikaria (**15**) |
| **Surface area (m²)** | 1. Thessaloniki (**387,319**)<br>2. East Attica (**315,318**)<br>3. North Athens Sector (**270,013**) | 1. Evrytania (**2,113**)<br>2. Ithaca (**2,264**)<br>3. Karpathos (**3,150**) |
| **Building volume (m³)** | 1. Thessaloniki (**2,168,014**)<br>2. West Attica (**1,431,710**)<br>3. East Attica (**1,361,519**) | 1. Evrytania (**6,718**)<br>2. Ithaca (**7,326**)<br>3. Karpathos (**10,991**) |
| **Storeys** | 1. East Attica (**1,645**)<br>2. Thessaloniki (**1,606**)<br>3. North Athens Sector (**1,226**) | 1. Grevena (**19**)<br>2. Kastoria (**20**)<br>3. Ithaca (**21**) |

*Note: Ithaca and Evrytania are tied at 11 new buildings. Geographic names are presented in English for accessibility. Rankings reflect the supplied 2025 data.*

---

## Dashboard features

### Visualizations and interactive controls

The table below summarizes each dashboard component. **Click any image to open the full-size preview.**

<table>
  <thead>
    <tr>
      <th align="left" width="20%">Visual / Control</th>
      <th align="left" width="55%">Description</th>
      <th align="center" width="25%">Preview</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td valign="middle"><strong>KPI cards</strong></td>
      <td valign="middle">Display Greece-wide totals for new buildings, storeys, total surface area (m²), and building volume (m³). Large values are expressed in millions for easier reading.</td>
      <td align="center" valign="middle">
        <a href="assets/kpi-visual.png">
          <img src="assets/kpi-visual.png" alt="KPI cards preview" width="160" />
        </a>
      </td>
    </tr>
    <tr>
      <td valign="middle"><strong>Geographic Shape Map</strong></td>
      <td valign="middle">Built using Power BI's <strong>Shape Map</strong> visual with two custom <strong>TopoJSON files</strong> defining Greece's regions and regional units. <strong>Bookmarks</strong> switch between geographic levels, while the <strong>metric slicer</strong> dynamically controls colour intensity, with darker shades indicating higher values. Geographic names are normalized for accurate map matching and readable Greek labels.</td>
      <td align="center" valign="middle">
        <a href="assets/map-visual.png">
          <img src="assets/map-visual.png" alt="Geographic Shape Map preview" width="160" />
        </a>
      </td>
    </tr>
    <tr>
      <td valign="middle"><strong>Treemap</strong></td>
      <td valign="middle">Uses rectangle size to compare each region or regional unit’s relative contribution to the selected measure. Larger rectangles indicate higher values.</td>
      <td align="center" valign="middle">
        <a href="assets/treemap-visual.png">
          <img src="assets/treemap-visual.png" alt="Treemap preview" width="160" />
        </a>
      </td>
    </tr>
    <tr>
      <td valign="middle"><strong>Horizontal ranking chart</strong></td>
      <td valign="middle">Ranks regions or regional units from highest to lowest according to the selected indicator, making geographic differences easy to compare.</td>
      <td align="center" valign="middle">
        <a href="assets/barchart-visual.png">
          <img src="assets/barchart-visual.png" alt="Horizontal ranking chart preview" width="160" />
        </a>
      </td>
    </tr>
    <tr>
      <td valign="middle"><strong>Scatter plot</strong></td>
      <td valign="middle">Plots the number of buildings on the horizontal axis against total surface area (m²) on the vertical axis. Each point represents a region or regional unit. This two-metric comparison remains fixed when the metric selector changes.</td>
      <td align="center" valign="middle">
        <a href="assets/scatterplot-visual.png">
          <img src="assets/scatterplot-visual.png" alt="Scatter plot preview" width="160" />
        </a>
      </td>
    </tr>
    <tr>
      <td valign="middle"><strong>Geographic level selector</strong></td>
      <td valign="middle">A Power BI bookmark navigator that switches between <strong>Regions</strong> (Περιφέρειες) and <strong>Regional Units</strong> (Περιφερειακές Ενότητες), updating the geographic detail shown in the visuals.</td>
      <td align="center" valign="middle">
        <a href="assets/region-slicer.png">
          <img src="assets/region-slicer.png" alt="Geographic level selector preview" width="160" />
        </a>
      </td>
    </tr>
    <tr>
      <td valign="middle"><strong>Metric selector</strong></td>
      <td valign="middle">A button-style slicer for <strong>Buildings</strong>, <strong>Surface Area</strong>, <strong>Volume</strong>, and <strong>Storeys</strong>. The choice updates the map, treemap, and ranking chart without changing the scatter plot axes.</td>
      <td align="center" valign="middle">
        <a href="assets/metric-slicer.png">
          <img src="assets/metric-slicer.png" alt="Metric selector preview" width="160" />
        </a>
      </td>
    </tr>
  </tbody>
</table>


### Dynamic chart labels

Visual titles and subtitles update according to the selected geographic level and construction metric. They explain what each chart shows and how to interpret its values (including m² and m³ where applicable). The scatter plot continues to compare buildings and surface area regardless of the metric selection.

---

## Data source

**Source:** [Hellenic Statistical Authority (ELSTAT)](https://www.statistics.gr/) — *New built-properties, storeys, volume and surface thereon, by region and regional unit* (Table 1, **January–December 2025**, final data).

The underlying data is publicly available and includes country totals, regional totals and regional-unit records, along with building counts, storeys, volume (m³) and surface area (m²).

---

## Data cleaning and preparation

The workflow starts with the original ELSTAT Excel files. **Microsoft Excel** is used for the initial cleaning and restructuring before importing the data into **Power BI**.

1. **Remove unnecessary metadata:** Delete the extra title rows, period notes, bilingual headings and other introductory material above the actual tabular data.
2. **Create a consistent table:** Retain the geographic names and four numeric measures under a clear, structured set of column headers.
3. **Add a `Category` column:** Distinguish `Country Total`, `Region` and `Regional Unit` records. This supports filtering by geographic level and prevents regional and regional-unit totals from being aggregated together.
4. **Add a `Date` column:** Assign a date reference to the reporting period to support future time-based modelling. In the current annual extract, `2025-01-01` identifies the **2025 reporting year**; it does **not** mean the figures were observed only in January.
5. **Normalize geographic names:** Standardize region and regional-unit labels, remove repetitive administrative prefixes from display names and adjust Greek place-name forms where needed so labels are consistent and readable across the map, charts and selectors.
6. **Model the data in Power BI:** Use category-aware DAX measures for national KPIs and a dynamic measure to drive the geographic map, treemap and ranking chart.

### Original vs. cleaned data

Click the previews to inspect the source table and the analysis-ready version.

<table>
  <tr>
    <th align="center" width="50%">Original ELSTAT Excel table</th>
    <th align="center" width="50%">Cleaned and structured table</th>
  </tr>
  <tr>
    <td align="center" valign="middle">
      <a href="assets/table-original.png">
        <img src="assets/table-original.png" alt="Original ELSTAT Excel worksheet with metadata and multi-row headers" width="100%" />
      </a>
    </td>
    <td align="center" valign="middle">
      <a href="assets/table-cleaned.png">
        <img src="assets/table-cleaned.png" alt="Cleaned Excel worksheet with Category and Date columns" width="100%" />
      </a>
    </td>
  </tr>
</table>

---

## Tools and techniques

- **Microsoft Excel:** Initial source-file cleaning and tabular restructuring.
- **Power BI Desktop:** Data modelling, relationships/filters and interactive report design.
- **DAX:** Measures for totals, dynamic metrics and context-aware chart titles and subtitles.
- **Bookmarks and slicers:** Navigation between geographic levels and interactive metric selection.

---

## Project Structure

```text
.
├── assets/                         # Images and visual assets
│
├── dashboard/
│   └── Greece-Construction-Analysis.pbix  # Power BI dashboard
│
├── data/
│   ├── dashboard_map_utils/        # Geographic boundaries for map visualizations
│   ├── processed/                  # Cleaned and transformed datasets
│   └── raw/                        # Original source datasets
│
├── data_processing/                # Data cleaning and transformation scripts
│
├── .gitignore
├── LICENSE
├── README.el.md                    # Greek documentation
└── README.md                       # English documentation
```

---

## Roadmap / TODO

- [ ] **Extend coverage beyond 2025:** Process the other publicly available ELSTAT new-building datasets for all available reporting months and years.
- [ ] **Standardize the historical files:** Apply a repeatable cleaning process, consistent geographic naming and a common data schema across reporting periods.
- [ ] **Add a proper time dimension:** Introduce a calendar/date table and **month** and **year** selectors, preserving the true granularity of each source period.
- [ ] **Enable time-based comparisons:** Compare construction activity month over month and year over year, both nationally and by region or regional unit.
- [ ] **Expand the dashboard with time-series visuals:** Add trends and period-over-period changes for buildings, storeys, volume and surface area.
- [ ] **Add English/Greek language switching:** Introduce a language selector that lets users switch between **English and Greek** throughout the dashboard, including visual titles, subtitles, navigation controls, metric labels and explanatory text, without changing the selected data or filters.

---

## Project status

**Current version:** Interactive Power BI analysis of the full **2025** reporting period, with region/regional-unit switching and dynamic metric selection.

**Next milestone:** A historical dataset and time-enabled dashboard for comparisons across months and years.
