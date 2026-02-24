import re

file_path = 'c:/Users/B-Zone/Documents/chem/first_chap/oxidation_valence.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS class
css_addition = '''
        /* Oxidation Tables */
        .oxidation-table {
            width: 100%;
            min-width: 600px;
            border-collapse: collapse;
            margin: 1rem 0;
            border: 1px solid var(--border-color);
            background: #fff;
        }

        .oxidation-table th {
            padding: 10px;
            border: 1px solid var(--border-color);
            background-color: var(--bg-sidebar);
            font-weight: 600;
            color: #1a2332;
        }

        .oxidation-table td {
            padding: 10px;
            border: 1px solid var(--border-color);
            text-align: center;
        }

        .oxidation-table td:not(:first-child) {
            text-align: left;
        }

        .oxidation-table .val-col,
        .oxidation-table .os-col {
            font-weight: bold;
            text-align: center !important;
        }

        /* Color classes for oxidation states */
        .os-base { color: #5A6A7B !important; }      /* Default/Zero */
        .os-low { color: #2ecc71 !important; }       /* +1, +2 (low positive) */
        .os-med { color: #d35400 !important; }       /* +3, +4 (medium positive) */
        .os-high { color: #8e44ad !important; }      /* +5, +6, +7 (high positive) */
        .os-neg { color: #2980b9 !important; }       /* Negative */
'''

if '.oxidation-table' not in content:
    content = content.replace('</style>', css_addition + '    </style>')

# Regex replacements
content = re.sub(
    r'<table\s+style="width:100%;(?: min-width: 600px;)? border-collapse: collapse; margin: (?:0\.5rem|1rem) 0; border: 1px solid var\(--border-color\);(?: text-align: center;)?">',
    '<table class="oxidation-table">',
    content
)

content = re.sub(
    r'<tr style="background-color: var\(--bg-sidebar\);">',
    '<tr>',
    content
)

content = re.sub(
    r'<th style="padding: (?:8|10)px; border: 1px solid var\(--border-color\);">',
    '<th>',
    content
)

content = re.sub(
    r'<td\s+style="text-align:center; padding: (?:8|10)px; border: 1px solid var\(--border-color\); font-weight: bold; color: #[a-fA-F0-9]{6};">\s*([+-]?\w+)\s*</td>',
    lambda m: f'<td class="os-col">{m.group(1)}</td>',
    content
)

content = re.sub(
    r'<td\s+style="padding: 10px; border: 1px solid var\(--border-color\); text-align: center; font-weight: bold; color: #[a-fA-F0-9]{6};">\s*([IVX]+)\s*</td>',
    lambda m: f'<td class="os-col">{m.group(1)}</td>',
    content
)

content = re.sub(
    r'<td style="padding: (?:8|10)px; border: 1px solid var\(--border-color\);(?: text-align: center;)?">',
    '<td>',
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete.")
