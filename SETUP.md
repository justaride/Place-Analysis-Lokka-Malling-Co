# Setup Guide - Aspelin Ramm Vulkan Oslo

Dette dokumentet beskriver hvordan du setter opp prosjektet for Aspelin Ramm sin portefølje på Vulkan.

## Status: ✅ KLAR TIL BRUK

Prosjektet er fullstendig konfigurert med:
- ✅ 4 eiendommer (Scandic Hotel Vulkan, Vulkan Arena, Bellonabygget, Nye Broverkstedet)
- ✅ Aktørdata for 3 eiendommer (70, 73, 68 aktører)
- ✅ Plaace screenshots (demografi, nøkkeltall, korthandel, besøkende, bevegelse, konkurransebildet)
- ✅ Hero-bilder og eiendomsbilder
- ✅ Aspelin Ramm logo

## Eiendommer i porteføljen

### 1. Scandic Hotel Vulkan ✅
- **Adresse:** Maridalsveien 13A, 0178 Oslo
- **Byggeår:** 2011 (utvidet 2022)
- **Areal:** 7 465 m²
- **Status:** Komplett med aktørdata (70 aktører)
- **Highlights:** Norges første hotell med energiklasse A, Svanemerket

### 2. Vulkan Arena ✅
- **Adresse:** Vulkan 26, 0178 Oslo
- **Byggeår:** 2010
- **Areal:** 1 400 m²
- **Status:** Komplett med aktørdata (73 aktører)
- **Highlights:** Konsert- og eventarena, kapasitet 800 stående

### 3. Bellonabygget ✅
- **Adresse:** Maridalsveien 13 / Vulkan 11, 0178 Oslo
- **Byggeår:** 2010–2011
- **Areal:** 3 120 m²
- **Status:** Komplett med aktørdata (68 aktører)
- **Highlights:** Norges første kontorbygg med energimerke A, FutureBuilt-forbilde

### 4. Nye Broverkstedet ⚠️
- **Adresse:** Vulkan 13 / Maridalsveien 17, 0178 Oslo
- **Byggeår:** 1960-tallet (under transformasjon)
- **Areal:** 9 179 m² (planlagt 14 000 m²)
- **Status:** Ingen aktørdata (utviklingsprosjekt)
- **Highlights:** Sirkulær transformasjon, bevaring av idrett og kultur

## Forutsetninger

- Node.js 18+ installert
- npm eller yarn pakkebehandler
- Git (for versjonskontroll)

## Installasjon

1. Installer avhengigheter:
```bash
cd place-analysis-aspelin-ramm
npm install
```

2. Opprett `.env.local` fil for miljøvariabler:
```bash
cp .env.example .env.local
```

3. Rediger `.env.local` og sett passord for innlogging:
```
SITE_PASSWORD=ditt-sikre-passord
```

## Kjøre lokalt

Start utviklingsserver:

```bash
npm run dev
```

Åpne [http://localhost:3000](http://localhost:3000) i nettleseren.

## Bygging for produksjon

```bash
npm run build
npm start
```

## Deployment

Prosjektet er optimalisert for Vercel:

1. Push til GitHub
2. Koble repository til Vercel
3. Sett miljøvariabel `SITE_PASSWORD` i Vercel dashboard
4. Deploy automatisk ved push til main branch

## Datastruktur

### Eiendomsdata

Alle eiendommer ligger i `/src/data/eiendommer/` som JSON-filer:
- `scandic-hotel-vulkan.json`
- `vulkan-arena.json`
- `bellonabygget.json`
- `nye-broverkstedet.json`

### Aktørdata

Aktørdata (næringsaktører i området) ligger i `/src/data/aktorer/`:
- `scandic-hotel-vulkan.json` (70 aktører)
- `vulkan-arena.json` (73 aktører)
- `bellonabygget.json` (68 aktører)

### Plaace screenshots

Screenshots fra Plaace-rapporter ligger i `/public/images/plaace/`:
- `scandic-hotel-vulkan/` (demografi.jpg, nokkeltall.jpg, etc.)
- `vulkan-arena/` (demografi.jpg, noekkeldata.jpg, etc.)
- `bellonabygget/` (demografi.jpg, noekkeldata.jpg, etc.)

### Hero-bilder

Hero-bilder for eiendommer ligger i `/public/images/`:
- `scandic-hotel-vulkan-hero.jpg`
- `vulkan-arena-hero.jpg`
- `bellonabygget.png`

## Legge til flere eiendommer

### 1. Opprett eiendoms-JSON

Opprett en ny JSON-fil i `/src/data/eiendommer/eiendomsnavn.json`:

```json
{
  "id": "eiendomsnavn",
  "navn": "Eiendomsnavn",
  "adresse": "Gateadresse, postnummer Oslo",
  "bydel": "Grünerløkka",
  "beskrivelse": "Kort beskrivelse",
  "byggeaar": 2010,
  "areal": 5000,
  "etasjer": 5,
  "arkitekt": "Arkitektnavn",
  "eier": "Aspelin Eiendom AS"
}
```

### 2. Legg til Plaace screenshots

Last opp screenshots i `/public/images/plaace/eiendomsnavn/`:
- `demografi.jpg`
- `nokkeltall.jpg` eller `noekkeldata.jpg`
- `korthandel.jpg`
- `besokende.jpg`
- `bevegelse.jpg`
- `konkurransebildet.jpg`

### 3. Prosesser aktørdata (valgfritt)

Hvis du har CSV-fil med aktører fra Plaace:

```bash
python3 scripts/process_aktor_csv.py "/path/to/aktører.csv" "eiendomsnavn"
```

Se [AKTOR_CSV_PROSESSERING_GUIDE.md](AKTOR_CSV_PROSESSERING_GUIDE.md) for detaljer.

### 4. Legg til hero-bilde

Kopier hero-bilde til `/public/images/eiendomsnavn-hero.jpg`

## Validering

Valider at alle data er korrekt formatert:

```bash
npm run validate:data
```

## Support

For spørsmål, kontakt:
- gabriel@naturalstate.no
- kim@naturalstate.no
- einar@naturalstate.no

---

*Oppdatert: 12. november 2025*
