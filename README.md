# propertymngmt2
Full scale version of proof of concept for distancing app URL is https://distancetg1.streamlit.app/ for as long as it's hosted there for free 

# Property Distance Sorter

A lightweight web application for selecting properties and instantly sorting them by distance to optimize routing, logistics, and operational planning.

This tool was built as a proof-of-concept to streamline property operations workflows such as inspections, vendor routing, snow removal planning, ski lease coordination, and field team dispatch.

---

## What This App Does

The Property Distance Sorter allows a user to:

- Upload an Excel file containing property names and distances
- Type and select any combination of properties (with autocomplete)
- Choose a sort direction (Closest → Farthest or Farthest → Closest)
- Instantly view the selected properties ordered by distance

The goal is to reduce manual sorting, mental math, and dependence on accuracy of unit zones when planning routes or grouping properties for operational efficiency.

---

## Tech Stack

This application is built entirely in **Python** using the following technologies:

### Core Framework
- **Streamlit** – for the web interface and UI components

### Data Handling
- **Pandas** – for reading, filtering, and sorting Excel data
- **OpenPyXL** – for Excel file support

### Frontend
- Streamlit’s built-in UI components (no React, no JavaScript frameworks)
- Custom CSS injected for branding and visual styling (lavender theme)

### Hosting
- **Streamlit Community Cloud** – free deployment platform connected to GitHub

---

## Why Streamlit?

Streamlit was chosen because it allows:

- Rapid prototyping without heavy frontend engineering
- Clean, interactive UIs using pure Python
- Easy deployment without infrastructure management
- Tight integration with data workflows (Excel, CSV, DataFrames)

This makes it ideal for internal tools, operations dashboards, and workflow automation.

---

## How It Works (High Level)

1. The user uploads an Excel file containing:
   - `Property Name`
   - `Distance` (numeric)

2. The app reads the file into a Pandas DataFrame.

3. The user types property names into a multiselect field:
   - Autocomplete suggests matches as they type
   - Multiple properties can be selected

4. The user chooses a sort order:
   - Closest → Farthest
   - Farthest → Closest

5. On clicking **Sort & Analyze**, the app:
   - Filters the DataFrame to the selected properties
   - Sorts by distance
   - Displays the ordered list in a clean, readable format

---

## Visual Design

The UI uses a soft lavender / purple theme with:
- Custom button styling
- Custom multiselect chip styling
- Custom radio button accents
- Branded favicon (mountain icon)

Styling is applied using injected CSS directly within the Streamlit app.

---

## Intended Use Cases

This tool is designed for scenarios such as:

- Optimizing hot tub service routes
- Planning inspection batches
- Coordinating snow removal dispatch
- Reducing drive time between properties
- Improving vendor scheduling efficiency

## Upcoming Use Cases
- Identify STR, Lease, or Both categorization of home
- Identify Unit Zone and Differentiating between TD 1, 2, 3, 4 quadrants
- Identify properties with null data 

While simple in concept, it forms the foundation for more advanced routing, zoning, and operational intelligence tooling.

---

## Project Structure

