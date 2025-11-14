# Malling&Co Place Analysis - Setup Guide

## Project Status

✅ **Project successfully created and pushed to GitHub!**

Repository: https://github.com/justaride/Place-Analysis-Lokka-Malling-Co

## What's Been Done

### 1. Project Structure
- Copied complete codebase from SPABO (Aspelin Ramm Vulkan) project
- All source code, components, and configuration files included
- Modern Next.js 16 + TypeScript + Tailwind CSS setup

### 2. Branding Updated
The following references have been changed from "Aspelin Ramm" to "Malling&Co" and "Vulkan" to "Grünerløkka":

- **README.md** - Updated project description
- **package.json** - Changed package name and description
- **src/app/layout.tsx** - Updated metadata and SEO
- **src/app/page.tsx** - Changed hero section text
- **src/app/om-prosjektet/page.tsx** - Updated project information
- **src/app/login/page.tsx** - Changed login page branding
- **src/app/sammenlign/page.tsx** - Updated comparison page metadata
- **src/components/layout/Header.tsx** - Changed logo reference and URL

### 3. Git & GitHub
- Initialized new git repository
- Created initial commit
- Pushed to GitHub: https://github.com/justaride/Place-Analysis-Lokka-Malling-Co

## Next Steps - Required Actions

### 🎨 1. Logo & Branding Assets
You need to add Malling&Co logo:

**Required file:**
- `public/images/malling-co-logo.png` - Main logo (recommended: 200-300px wide, transparent background)

**Optional files:**
- `public/images/malling-co-logo.svg` - SVG version for better scaling

**Current status:** Header references `/images/malling-co-logo.png` but file doesn't exist yet.

**Note:** The old Aspelin Ramm logos are still in the public/images folder and can be removed:
- `public/images/aspelin-ramm-logo.png`
- `public/images/aspelin-ramm-logo.svg`
- `public/images/aspelin-ramm-logo-new.svg`

### 🏢 2. Property Data Migration
The project currently contains Vulkan properties (from SPABO project). You need to:

**A. Remove old properties:**
These files are from the Vulkan portfolio and should be removed or replaced:
```
src/data/eiendommer/
  - bellonabygget.json
  - nye-broverkstedet.json
  - scandic-hotel-vulkan.json
  - vulkan-arena.json

src/data/aktorer/
  - bellonabygget.json
  - nye-broverkstedet.json
  - scandic-hotel-vulkan.json
  - vulkan-arena.json

public/images/plaace/
  - bellonabygget/
  - nye-broverkstedet/
  - scandic-hotel-vulkan/
  - vulkan-arena/

public/pdf/brenneriveien-5/
  (Brenneriveien 5 PDFs - SPABO property)
```

**B. Add Malling&Co properties:**
For each Malling&Co property on Grünerløkka, create:
1. Property data JSON file (see `docs/DATASTRUKTUR.md` for format)
2. Plaace screenshots (6 images per property)
3. PDF reports (if available)
4. Property images (hero, map, thumbnail)

**See:** `docs/LEGG-TIL-EIENDOM.md` for detailed instructions on adding properties.

### 🔑 3. Environment Configuration
1. Copy `.env.example` to `.env.local`
2. Set password for the site:
   ```
   SITE_PASSWORD=your-secure-password-here
   ```

### 📦 4. Installation & Development
```bash
cd /Users/gabrielboen/Place-Analysis-Lokka-Malling-Co

# Install dependencies
npm install

# Run development server
npm run dev
```

The site will be available at http://localhost:3000

### 🌐 5. Company Information Update
Update the company URL in Header component:
- Currently links to `https://mallingco.com`
- Verify this is the correct Malling&Co website URL
- Update if needed in: `src/components/layout/Header.tsx`

### 📝 6. Content Updates Needed
The following files contain SPABO-specific content that should be reviewed and updated:

**High Priority:**
- `src/components/eiendom/EiendomsprofilContent.tsx` - Contains detailed Brenneriveien 5 (SPABO) property profile
- Documentation files that reference Brenneriveien 5 or SPABO specifics

**Low Priority:**
- Footer text/links (if any company-specific content)
- Any remaining references to Vulkan that should be Grünerløkka

## Project Structure Overview

```
Place-Analysis-Lokka-Malling-Co/
├── src/
│   ├── app/               # Next.js pages and routes
│   ├── components/        # React components
│   ├── data/             # Property and actor data (JSON)
│   ├── lib/              # Utility functions
│   └── types/            # TypeScript definitions
├── public/
│   ├── images/           # Logos, property images, Plaace screenshots
│   └── pdf/              # PDF reports
├── docs/                 # Documentation
└── scripts/              # Utility scripts
```

## Key Documentation Files

- `docs/LEGG-TIL-EIENDOM.md` - How to add new properties
- `docs/DATASTRUKTUR.md` - Data structure specifications
- `docs/DEPLOYMENT.md` - Deployment guide
- `AKTOR_CSV_PROSESSERING_GUIDE.md` - Processing CSV data for actors

## Deployment

The project is configured for Vercel deployment. See `docs/DEPLOYMENT.md` for details.

## Support

This is a Natural State project for Malling&Co, based on the successful SPABO/Aspelin Ramm implementation.

For questions about the technical setup, refer to the documentation files or the original SPABO project.

---

**Next immediate action:** Add Malling&Co logo to `public/images/malling-co-logo.png` and test the development server with `npm run dev`.
