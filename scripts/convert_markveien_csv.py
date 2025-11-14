#!/usr/bin/env python3
"""
Convert Markveien 35 CSV to JSON format for actors
"""

import csv
import json
import re

def parse_value(text):
    """Extract numeric value from text like 'NOK 87 mill.'"""
    if not text or text == '-':
        return None
    match = re.search(r'(\d+)', text)
    return int(match.group(1)) if match else None

def parse_percentage(text):
    """Extract percentage from text like '0.3%'"""
    if not text or text == '-' or text.strip() == '-':
        return None
    match = re.search(r'([-\d.]+)', text)
    if match:
        try:
            value = match.group(1)
            if value == '-':
                return None
            return float(value)
        except ValueError:
            return None
    return None

def parse_employees(text):
    """Parse employee data like '21\n\n9767 i 503 lokasjoner'"""
    if not text or text == '-':
        return None, None, None

    lines = [line.strip() for line in text.split('\n') if line.strip()]
    local = int(lines[0]) if lines and lines[0].isdigit() else 0

    chain = None
    locations = None
    if len(lines) > 1:
        match = re.search(r'(\d+)\s+i\s+(\d+)', lines[1])
        if match:
            chain = int(match.group(1))
            locations = int(match.group(2))

    return local, chain, locations

def convert_csv_to_json(csv_path, json_path):
    actors = []

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            rank = row.get('#', '').strip()
            if not rank or not rank.startswith('#'):
                continue

            omsetning = parse_value(row.get('Omsetning', ''))
            kjede_prosent = row.get('Omsetning', '').split('\n')[-1].strip() if '\n' in row.get('Omsetning', '') else None
            yoy_vekst = parse_percentage(row.get('YoY-vekst', ''))
            ansatte_lokalt, ansatte_kjede, kjede_lokasjoner = parse_employees(row.get('Ansatte', ''))
            markedsandel = parse_percentage(row.get('Markedsandel', ''))

            actor = {
                "rank": rank,
                "navn": row.get('Navn', '').strip(),
                "type": row.get('Type', '').strip(),
                "adresse": row.get('Adresse', '').strip().upper(),
                "kommune": row.get('Kommune', '').strip(),
                "omsetning": omsetning,
                "kjedeProsent": kjede_prosent,
                "yoyVekst": yoy_vekst,
                "ansatteLokalt": ansatte_lokalt,
                "ansatteKjede": ansatte_kjede,
                "kjedeLokasjoner": kjede_lokasjoner,
                "markedsandel": markedsandel
            }

            actors.append(actor)

    output = {"actors": actors}

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Converted {len(actors)} actors from {csv_path} to {json_path}")

if __name__ == '__main__':
    csv_path = '/Users/gabrielboen/Place-Analysis-Lokka-Malling-Co/src/data/aktorer/markveien-35.csv'
    json_path = '/Users/gabrielboen/Place-Analysis-Lokka-Malling-Co/src/data/aktorer/markveien-35.json'

    convert_csv_to_json(csv_path, json_path)
