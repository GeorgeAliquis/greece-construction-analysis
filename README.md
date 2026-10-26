# Greece Construction Activity | 2025
## Overview
An interactive **Power BI dashboard** exploring new building activity across Greece in **2025**, using publicly available data from the **Hellenic Statistical Authority (ELSTAT)**.

The project transforms ELSTAT's published Excel tables into a clean, analysis-ready dataset and makes it possible to compare construction activity at two geographic levels: **regions** and **regional units**. The current report covers **January–December 2025**; expanding it into a multi-year, monthly time-series analysis is the next major goal.

## Dashboard previews

The dashboard is presented in Greek to preserve the names of administrative areas and make the analysis accessible to a Greek-speaking audience. **Click either preview to view it at full size.**

<table>
  <tr>
    <th align="center" width="50%">Regions</th>
    <th align="center" width="50%">Regional units</th>
  </tr>
  <tr>
    <td align="center" valign="top">
      <a href="assets/greece-construction-analysis-regions-dashboard-v1.png">
        <img src="assets/greece-construction-analysis-regions-dashboard-v1.png" alt="Power BI construction dashboard displaying Greek regions" width="100%" />
      </a>
    </td>
    <td align="center" valign="top">
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

## Project overview

The analysis examines four measures of newly built properties:

| Indicator | Greece, 2025 |
| --- | ---: |
| New buildings | **11,650** |
| Storeys | **24,292** |
| Total building volume | **20,608,577 m³** |
| Total building surface area | **4,731,479 m²** |

These figures describe the **2025 reporting period**, not a monthly trend. Geographic comparisons use the appropriate administrative level to avoid counting the same activity twice through both region and regional-unit rows.

## Dashboard features

### Visualizations

- **KPI cards:** Show national totals for new buildings, storeys, surface area and volume. Large surface-area and volume values are displayed in millions for readability.
- **Geographic map:** Uses colour intensity to show where the selected construction measure is concentrated. Darker shades indicate higher values; units change appropriately between building/storey counts, m² and m³.
- **Treemap:** Compares the relative size of each geographic area's contribution to the selected indicator. Larger rectangles represent higher values.
- **Horizontal ranking chart:** Ranks regions or regional units by the selected measure, making the highest and lowest values easy to identify.
- **Scatter plot:** Compares **number of buildings (horizontal axis)** with **total surface area in m² (vertical axis)**. Each point represents a region or regional unit, depending on the chosen geographic level. Unlike the other three analytical charts, this comparison remains fixed when the metric selector changes.

### Geographic map configuration

The geographic visualization is built with Power BI's **Shape Map** visual and **two custom TopoJSON files**, one for each administrative level:

- **Regions TopoJSON:** Defines the boundaries of Greece's regions (*Περιφέρειες*).
- **Regional units TopoJSON:** Defines the more detailed boundaries of Greece's regional units (*Περιφερειακές Ενότητες*).

Each map uses the corresponding boundary file so the displayed shapes match the selected level of analysis. **Power BI bookmarks** switch between the region-level and regional-unit-level map visuals, while the **metric slicer** changes the measure represented by their colour intensity. The same geographic-level switch is applied to the accompanying charts.

Geographic names are also **normalized for reliable matching** between the cleaned ELSTAT data and the TopoJSON map identifiers. User-facing labels are simplified to make Greek region and regional-unit names easier to read throughout the dashboard.

### Interactive controls

- **Geographic level selector:** Switches the analysis between **Regions** and **Regional Units** using Power BI bookmarks.
- **Metric selector:** Switches between **Buildings**, **Surface Area**, **Volume** and **Storeys**. It updates the geographic map, treemap and ranking chart without changing the scatter plot's two-axis comparison.
- **Dynamic chart titles and subtitles:** Describe the current selection and explain how each visualization should be read, including the relevant measurement units.

## Data source

**Source:** [Hellenic Statistical Authority (ELSTAT)](https://www.statistics.gr/) — *New built-properties, storeys, volume and surface thereon, by region and regional unit* (Table 1, **January–December 2025**, final data).

The underlying data is publicly available and includes country totals, regional totals and regional-unit records, along with building counts, storeys, volume (m³) and surface area (m²).

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
    <td align="center" valign="top">
      <a href="assets/table-original.png">
        <img src="assets/table-original.png" alt="Original ELSTAT Excel worksheet with metadata and multi-row headers" width="100%" />
      </a>
    </td>
    <td align="center" valign="top">
      <a href="assets/table-cleaned.png">
        <img src="assets/table-cleaned.png" alt="Cleaned Excel worksheet with Category and Date columns" width="100%" />
      </a>
    </td>
  </tr>
</table>

## Tools and techniques

- **Microsoft Excel:** Initial source-file cleaning and tabular restructuring.
- **Power BI Desktop:** Data modelling, relationships/filters and interactive report design.
- **DAX:** Measures for totals, dynamic metrics and context-aware chart titles and subtitles.
- **Bookmarks and slicers:** Navigation between geographic levels and interactive metric selection.

## Roadmap / TODO

- [ ] **Extend coverage beyond 2025:** Process the other publicly available ELSTAT new-building datasets for all available reporting months and years.
- [ ] **Standardize the historical files:** Apply a repeatable cleaning process, consistent geographic naming and a common data schema across reporting periods.
- [ ] **Add a proper time dimension:** Introduce a calendar/date table and **month** and **year** selectors, preserving the true granularity of each source period.
- [ ] **Enable time-based comparisons:** Compare construction activity month over month and year over year, both nationally and by region or regional unit.
- [ ] **Expand the dashboard with time-series visuals:** Add trends and period-over-period changes for buildings, storeys, volume and surface area.
- [ ] **Add English/Greek language switching:** Introduce a language selector that lets users switch between **English and Greek** throughout the dashboard, including visual titles, subtitles, navigation controls, metric labels and explanatory text, without changing the selected data or filters.

## Project status

**Current version:** Interactive Power BI analysis of the full **2025** reporting period, with region/regional-unit switching and dynamic metric selection.

**Next milestone:** A historical dataset and time-enabled dashboard for comparisons across months and years.
