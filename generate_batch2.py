#!/usr/bin/env python3
"""
Generate JSON-LD schemas for Top Cable Batch 2 (10 cables × multiple languages)
Following v5.1 specification with rules 13-16
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# SHARED STRUCTURES (same as Batch 1)
# ============================================================

ORGANIZATION = {
    "@type": "Organization",
    "@id": "https://www.topcable.com/#organization",
    "name": "Top Cable",
    "url": "https://www.topcable.com/",
    "email": "sales@topcable.com",
    "telephone": "+34 935 880 911",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Leonardo da Vinci, 1",
        "addressLocality": "Rubí",
        "addressRegion": "Barcelona",
        "postalCode": "08191",
        "addressCountry": "ES"
    },
    "logo": {
        "@type": "ImageObject",
        "@id": "https://www.topcable.com/#logo",
        "url": "https://www.topcable.com/wp-content/uploads/2026/01/top-cable-logo.png",
        "contentUrl": "https://www.topcable.com/wp-content/uploads/2026/01/top-cable-logo.png"
    },
    "sameAs": [
        "https://www.linkedin.com/company/topcable/",
        "https://www.youtube.com/@Topcable_europe",
        "https://www.instagram.com/topcable_spain/",
        "https://www.facebook.com/topcable/"
    ]
}

VALUE_PROPS = {
    "en": [
        {"name": "European Stock", "value": "Largest European Stock Holding"},
        {"name": "Manufacturing Quality", "value": "As cable manufacturers, we ensure cost-effective premium quality and lasting performance."},
        {"name": "Quality Testing", "value": "Our in-house labs guarantee rigorous cable quality, reliability, and standards compliance."},
        {"name": "Global Logistics", "value": "Global cable delivery solutions—expert logistics for seamless supply."},
        {"name": "Fast Delivery", "value": "Full cable stock, ready for fast delivery- shortest lead times."},
        {"name": "Sustainability", "value": "EPD-certified cables: Sustainable manufacturing for your Scope 3 success."},
        {"name": "Customer Service", "value": "Expert, friendly and professional sales team offering a fast & efficient customer service. Global customers are welcome!"},
    ],
    "fr": [
        {"name": "Stock européen", "value": "Le plus grand stock européen de câbles"},
        {"name": "Qualité de fabrication", "value": "En tant que fabricants de câbles, nous garantissons une qualité premium rentable et des performances durables."},
        {"name": "Contrôle de qualité", "value": "Nos laboratoires internes garantissent une qualité rigoureuse des câbles, fiabilité et conformité aux normes."},
        {"name": "Logistique mondiale", "value": "Solutions logistiques mondiales pour câbles — expertise logistique pour un approvisionnement sans faille."},
        {"name": "Livraison rapide", "value": "Stock complet de câbles, prêt pour une livraison rapide — délais les plus courts."},
        {"name": "Durabilité", "value": "Câbles certifiés EPD : fabrication durable pour votre succès Scope 3."},
        {"name": "Service client", "value": "Équipe commerciale experte, conviviale et professionnelle offrant un service client rapide et efficace. Clients internationaux bienvenus !"},
    ],
    "es": [
        {"name": "Stock europeo", "value": "El mayor stock europeo de cables"},
        {"name": "Calidad de fabricación", "value": "Como fabricantes de cables, garantizamos una calidad premium rentable y un rendimiento duradero."},
        {"name": "Control de calidad", "value": "Nuestros laboratorios internos garantizan una rigurosa calidad del cable, fiabilidad y cumplimiento normativo."},
        {"name": "Logística mundial", "value": "Soluciones logísticas mundiales para cables — experiencia logística para un suministro sin interrupciones."},
        {"name": "Entrega rápida", "value": "Stock completo de cables, listo para entrega rápida — plazos de entrega más cortos."},
        {"name": "Sostenibilidad", "value": "Cables con certificación EPD: fabricación sostenible para su éxito en Scope 3."},
        {"name": "Atención al cliente", "value": "Equipo comercial experto, cercano y profesional ofreciendo una atención al cliente rápida y eficiente. ¡Clientes internacionales bienvenidos!"},
    ],
}

CATEGORIES = {
    "en": "Hardware > Building Materials > Wiring & Cables > Electrical Cables",
    "fr": "Quincaillerie > Matériaux de construction > Câblage et câbles > Câbles électriques",
    "es": "Ferretería > Materiales de construcción > Cableado y cables > Cables eléctricos",
}

AUDIENCE_INDUSTRIAL = {
    "en": "Electrical Distributors, Electrical Installers, Engineers (Industrial Projects)",
    "fr": "Distributeurs électriques, Installateurs électriques, Ingénieurs (Projets industriels)",
    "es": "Distribuidores eléctricos, Instaladores eléctricos, Ingenieros (Proyectos industriales)",
}
AUDIENCE_LSZH = {
    "en": "Electrical Distributors, Electrical Installers, Engineers (Public Buildings & Hospitals), Engineers (Industrial Projects), Data Centre Operators, Data Centre Design Consultants, Data Centre Contractors, Data Centre Installers",
    "fr": "Distributeurs électriques, Installateurs électriques, Ingénieurs (Bâtiments publics et hôpitaux), Ingénieurs (Projets industriels), Opérateurs de centres de données, Consultants en conception de centres de données, Entrepreneurs de centres de données, Installateurs de centres de données",
    "es": "Distribuidores eléctricos, Instaladores eléctricos, Ingenieros (Edificios públicos y hospitales), Ingenieros (Proyectos industriales), Data Centre Operators, Data Centre Design Consultants, Data Centre Contractors, Data Centre Installers",
}
AUDIENCE_DOMESTIC = {
    "en": "Electrical Distributors, Electrical Installers, Engineers (Domestic & Commercial Buildings)",
    "fr": "Distributeurs électriques, Installateurs électriques, Ingénieurs (Bâtiments domestiques et commerciaux)",
    "es": "Distribuidores eléctricos, Instaladores eléctricos, Ingenieros (Edificios domésticos y comerciales)",
}

MATERIAL_COPPER_FLEX = {
    "en": "Copper, class 5 (flexible)",
    "fr": "Cuivre, classe 5 (souple)",
    "es": "Cobre, clase 5 (flexible)",
}
MATERIAL_ALUMINIUM_CL2 = {
    "en": "Aluminium, class 2",
    "fr": "Aluminium, classe 2",
    "es": "Aluminio, clase 2",
}

BREADCRUMB_FAMILIES = {
    "rubber": {
        "en": {"name": "Rubber Cables", "url": "https://www.topcable.com/rubber-cables/"},
        "fr": {"name": "Câbles en caoutchouc", "url": "https://www.topcable.com/fr/cables-en-caoutchouc/"},
        "es": {"name": "Cables de goma", "url": "https://www.topcable.com/es/cables-de-goma/"},
    },
    "power": {
        "en": {"name": "Power Cables", "url": "https://www.topcable.com/power-cables/"},
        "fr": {"name": "Câbles d'énergie", "url": "https://www.topcable.com/fr/cables-denergie/"},
        "es": {"name": "Cables de energía", "url": "https://www.topcable.com/es/cables-de-energia/"},
    },
    "lszh": {
        "en": {"name": "LSZH Cables", "url": "https://www.topcable.com/lszh-cables/"},
        "fr": {"name": "Câbles LSZH", "url": "https://www.topcable.com/fr/cables-lszh/"},
        "es": {"name": "Cables LSZH", "url": "https://www.topcable.com/es/cables-lszh/"},
    },
    "pvc": {
        "en": {"name": "PVC Cables", "url": "https://www.topcable.com/pvc-cables/"},
        "fr": {"name": "Câbles PVC", "url": "https://www.topcable.com/fr/cables-pvc/"},
        "es": {"name": "Cables PVC", "url": "https://www.topcable.com/es/cables-pvc/"},
    },
}

BRAND_URLS = {
    "en": "https://www.topcable.com/company/our-brands/",
    "fr": "https://www.topcable.com/fr/company/nos-marques/",
    "es": "https://www.topcable.com/company/our-brands/",
}

HOME = {
    "en": {"name": "Home", "url": "https://www.topcable.com/"},
    "fr": {"name": "Accueil", "url": "https://www.topcable.com/fr/"},
    "es": {"name": "Inicio", "url": "https://www.topcable.com/es/"},
}

SUBJECT_OF = {
    "en": {
        "name_prefix": "Technical Datasheet - ",
        "description": "Complete technical specifications, engineering data and certifications for the cable.",
    },
    "fr": {
        "name_prefix": "Fiche Technique - ",
        "description": "Spécifications techniques complètes, données d'ingénierie et certifications du câble.",
    },
    "es": {
        "name_prefix": "Ficha Técnica - ",
        "description": "Especificaciones técnicas completas, datos de ingeniería y certificaciones del cable.",
    },
}

PROP_NAMES = {
    "en": {
        "conductor": "Conductor",
        "insulation": "Insulation",
        "outer_sheath": "Outer Sheath",
        "inner_covering": "Inner Covering",
        "armour": "Armour",
        "screen": "Screen",
        "separation_sheath": "Separation Sheath / Bedding",
        "rated_voltage": "Rated Voltage",
        "max_temp": "Maximum Conductor Temperature",
        "max_sc_temp": "Maximum Short-Circuit Temperature",
        "min_service_temp": "Minimum Service Temperature",
        "min_install_temp": "Minimum Installation Temperature",
        "flame_nonprop": "Flame Non-Propagation",
        "fire_nonprop": "Fire Non-Propagation",
        "cpr": "CPR Classification",
        "halogen_free": "Halogen Free",
        "low_corrosive_gases": "Low Corrosive Gases Emission",
        "low_smoke": "Low Smoke Emission",
        "light_transmittance": "Light Transmittance",
        "fire_resistant": "Fire Resistant",
        "reduced_halogens": "Reduced Halogens",
        "min_bending": "Minimum Bending Radius",
        "impact": "Impact Resistance",
        "rodent_proof": "Rodent Proof",
        "chemical_oil": "Chemical & Oil Resistance",
        "uv": "UV Resistance",
        "hydrocarbon": "Hydrocarbon Resistance",
        "water": "Water Resistance",
        "installation": "Installation Conditions",
        "standards_ref": "Standards (According To)",
        "standards_approvals": "Standards and Approvals",
        "applications": "Typical Applications",
        "atex": "ATEX",
    },
    "fr": {
        "conductor": "Conducteur",
        "insulation": "Isolation",
        "outer_sheath": "Gaine extérieure",
        "inner_covering": "Gaine intérieure",
        "armour": "Armure",
        "screen": "Écran",
        "separation_sheath": "Gaine de séparation / Bourrage",
        "rated_voltage": "Tension nominale",
        "max_temp": "Température maximale du conducteur",
        "max_sc_temp": "Température maximale de court-circuit",
        "min_service_temp": "Température minimale de service",
        "min_install_temp": "Température minimale d'installation",
        "flame_nonprop": "Non-propagation de la flamme",
        "fire_nonprop": "Non-propagation de l'incendie",
        "cpr": "Classification CPR",
        "halogen_free": "Sans halogène",
        "low_corrosive_gases": "Faible émission de gaz corrosifs",
        "low_smoke": "Faible émission de fumée",
        "light_transmittance": "Transmittance lumineuse",
        "fire_resistant": "Résistance au feu",
        "reduced_halogens": "Halogènes réduits",
        "min_bending": "Rayon de courbure minimum",
        "impact": "Résistance aux chocs",
        "rodent_proof": "Anti-rongeurs",
        "chemical_oil": "Résistance chimique et aux huiles",
        "uv": "Résistance aux UV",
        "hydrocarbon": "Résistance aux hydrocarbures",
        "water": "Résistance à l'eau",
        "installation": "Conditions d'installation",
        "standards_ref": "Normes (Selon)",
        "standards_approvals": "Normes et approbations",
        "applications": "Applications typiques",
        "atex": "ATEX",
    },
    "es": {
        "conductor": "Conductor",
        "insulation": "Aislamiento",
        "outer_sheath": "Cubierta exterior",
        "inner_covering": "Cubierta interior",
        "armour": "Armadura",
        "screen": "Pantalla",
        "separation_sheath": "Cubierta de separación / Relleno",
        "rated_voltage": "Tensión nominal",
        "max_temp": "Temperatura máxima del conductor",
        "max_sc_temp": "Temperatura máxima de cortocircuito",
        "min_service_temp": "Temperatura mínima de servicio",
        "min_install_temp": "Temperatura mínima de instalación",
        "flame_nonprop": "No propagación de la llama",
        "fire_nonprop": "No propagación del incendio",
        "cpr": "Clasificación CPR",
        "halogen_free": "Libre de halógenos",
        "low_corrosive_gases": "Baja emisión de gases corrosivos",
        "low_smoke": "Baja emisión de humo",
        "light_transmittance": "Transmitancia luminosa",
        "fire_resistant": "Resistencia al fuego",
        "reduced_halogens": "Halógenos reducidos",
        "min_bending": "Radio mínimo de curvatura",
        "impact": "Resistencia al impacto",
        "rodent_proof": "Anti-roedores",
        "chemical_oil": "Resistencia química y a aceites",
        "uv": "Resistencia a los UV",
        "hydrocarbon": "Resistencia a los hidrocarburos",
        "water": "Resistencia al agua",
        "installation": "Condiciones de instalación",
        "standards_ref": "Normas (Según)",
        "standards_approvals": "Normas y aprobaciones",
        "applications": "Aplicaciones típicas",
        "atex": "ATEX",
    },
}


def make_prop(lang, key, value, unit=None, url=None):
    p = {"@type": "PropertyValue", "name": PROP_NAMES[lang][key], "value": value}
    if unit:
        p["unitText"] = unit
    if url:
        p["url"] = url
    return p


def make_value_props(lang):
    return [{"@type": "PropertyValue", "name": vp["name"], "value": vp["value"]} for vp in VALUE_PROPS[lang]]


def build_schema(cable, lang):
    d = cable["data"][lang]
    c = cable["common"]
    if lang == "en":
        page_url = f"https://www.topcable.com/cable/{c['slug']}/"
    else:
        page_url = f"https://www.topcable.com/{lang}/cable/{c['slug']}/"
    ds_slug = c.get("datasheet_slug", c["slug"])
    datasheet_url = f"https://www.topcable.com/downloads/pdf/{lang}/topcable-datasheet-{ds_slug}-{lang}.pdf"

    product = {
        "@type": "Product",
        "name": d["name"],
        "mpn": c["mpn"],
        "sku": c["mpn"],
        "description": d["description"],
        "image": c["images"],
        "url": page_url,
        "category": CATEGORIES[lang],
        "brand": {
            "@type": "Brand",
            "name": c["brand"],
            "url": BRAND_URLS[lang],
        },
        "manufacturer": {
            "@type": "Organization",
            "@id": "https://www.topcable.com/#organization"
        },
        "material": d["material"],
        "audience": {
            "@type": "BusinessAudience",
            "audienceType": d["audience"],
        },
        "subjectOf": {
            "@type": "DigitalDocument",
            "name": SUBJECT_OF[lang]["name_prefix"] + d["name"],
            "url": datasheet_url,
            "encodingFormat": "application/pdf",
            "description": SUBJECT_OF[lang]["description"],
        },
        "additionalProperty": d["properties"] + make_value_props(lang),
        "offers": {
            "@type": "Offer",
            "url": page_url,
            "priceCurrency": "EUR",
            "price": 0,
            "availability": "https://schema.org/InStock",
            "itemCondition": "https://schema.org/NewCondition",
            "eligibleRegion": {
                "@type": "Place",
                "name": "World"
            },
            "seller": {
                "@type": "Organization",
                "@id": "https://www.topcable.com/#organization"
            }
        }
    }

    family = c["family"]
    bf = BREADCRUMB_FAMILIES[family][lang]
    breadcrumb = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": HOME[lang]["name"], "item": HOME[lang]["url"]},
            {"@type": "ListItem", "position": 2, "name": bf["name"], "item": bf["url"]},
            {"@type": "ListItem", "position": 3, "name": d["name"]}
        ]
    }

    return {"@context": "https://schema.org", "@graph": [product, breadcrumb, ORGANIZATION]}


# ============================================================
# SHARED TRANSLATION HELPERS
# ============================================================
ELECTROPEDIA_URL = "https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=151-12-05"

CONDUCTOR_COPPER_FLEX = {
    "en": "Electrolytic annealed copper, class 5 (flexible) according to EN 60228 and IEC 60228",
    "fr": "Cuivre électrolytique, classe 5 (souple) selon EN 60228 et IEC 60228",
    "es": "Cobre electrolítico recocido, clase 5 (flexible) según UNE-EN 60228 e IEC 60228",
}
CONDUCTOR_ALUMINIUM_CL2 = {
    "en": "Aluminium, class 2 according to EN 60228 and IEC 60228",
    "fr": "Aluminium, classe 2 selon EN 60228 et IEC 60228",
    "es": "Aluminio, clase 2 según UNE-EN 60228 e IEC 60228",
}

SC_TEMP_250 = {"en": "250 (max. 5 s)", "fr": "250 (max. 5 s)", "es": "250 (máximo 5 s)"}
SC_TEMP_160 = {"en": "160 (max. 5 s)", "fr": "160 (max. 5 s)", "es": "160 (máximo 5 s)"}

MIN_TEMP_FIXED = {
    "en": "-40 (fixed and protected installations)",
    "fr": "-40 (installations fixes et protégées)",
    "es": "-40 (estático con protección)",
}
MIN_TEMP_FIXED_MOBILE_25 = {
    "en": "-40 (fixed and protected installations) and -25 (mobile use)",
    "fr": "-40 (installations fixes et protégées) et -25 (service mobile)",
    "es": "-40 (estático con protección) y -25 (servicio móvil)",
}

FLAME_NONPROP = {
    "en": "Flame non-propagation according to EN 60332-1 / IEC 60332-1",
    "fr": "Non-propagation de la flamme selon EN 60332-1 et IEC 60332-1",
    "es": "No propagación de la llama según UNE-EN 60332-1 / IEC 60332-1",
}
FIRE_NONPROP = {
    "en": "Fire non-propagation according to EN 60332-3 / IEC 60332-3 and EN 50399",
    "fr": "Non-propagation de l'incendie selon EN 60332-3 et IEC 60332-3 et EN 50399",
    "es": "No propagación del incendio según UNE-EN 60332-3 / IEC 60332-3 y EN 50399",
}
FIRE_NONPROP_3_24 = {
    "en": "Fire non-propagation according to EN 60332-3-24 / IEC 60332-3-24 and EN 50399",
    "fr": "Non-propagation de l'incendie selon EN 60332-3-24 et IEC 60332-3-24 et EN 50399",
    "es": "No propagación del incendio según UNE-EN 60332-3-24 / IEC 60332-3-24 y EN 50399",
}

HALOGEN_FREE = {
    "en": "Halogen free according to EN 60754-1 / IEC 60754-1",
    "fr": "Sans halogène selon EN 60754-1 et IEC 60754-1",
    "es": "Libre de halógenos según EN 60754-1 / IEC 60754-1",
}
LOW_CORROSIVE_GASES = {
    "en": "Low corrosive gases emission according to EN 60754-2 / IEC 60754-2",
    "fr": "Faible émission de gaz corrosifs selon EN 60754-2 et IEC 60754-2",
    "es": "Baja emisión de gases corrosivos según EN 60754-2 / IEC 60754-2",
}
LOW_SMOKE_61034 = {
    "en": "Low smoke emission according to UNE-EN 61034 / IEC 61034",
    "fr": "Faible émission de fumée selon UNE-EN 61034 et IEC 61034",
    "es": "Baja emisión de humo según UNE-EN 61034 / IEC 61034",
}

IMPACT_AG2 = {"en": "AG2 Medium severity", "fr": "AG2 Sévérité moyenne", "es": "AG2 Medio"}
IMPACT_AG4 = {"en": "AG4 High severity", "fr": "AG4 Sévérité élevée", "es": "AG4 Severidad alta"}

CHEM_EXCELLENT = {
    "en": "Excellent. Grease & mineral oils resistance: Excellent",
    "fr": "Excellente. Résistance aux graisses et huiles minérales : Excellente",
    "es": "Excelente. Resistencia a grasas y aceites minerales: Excelente",
}
CHEM_GOOD = {"en": "Good", "fr": "Bonne", "es": "Buena"}
CHEM_ACCEPTABLE = {"en": "Acceptable", "fr": "Acceptable", "es": "Aceptable"}

UV_EN50618 = {
    "en": "UV Resistant according to EN 50618",
    "fr": "Résistance aux UV selon EN 50618",
    "es": "Resistencia a los rayos ultravioleta según EN 50618",
}
UV_UNE211605 = {
    "en": "UV Resistant according to UNE 211605",
    "fr": "Résistance aux UV selon UNE 211605",
    "es": "Resistencia a los rayos ultravioleta según UNE 211605",
}
UV_HD603 = {
    "en": "UV Resistant according to HD 603-1",
    "fr": "Résistance aux UV selon HD 603-1",
    "es": "Resistencia a los rayos ultravioleta según HD 603-1",
}

WATER_AD8 = {"en": "AD8 Submersion", "fr": "AD8 Submersion", "es": "AD8 Sumersión"}
WATER_AD7 = {"en": "AD7 Immersion", "fr": "AD7 Immersion", "es": "AD7 Inmersión"}
WATER_AD5 = {"en": "AD5 Jets", "fr": "AD5 Jets", "es": "AD5 Chorros"}

INSTALL_FULL = {
    "en": "Open Air. Buried. In conduit.",
    "fr": "À l'air libre. Enterré. En canalisation.",
    "es": "Al aire. Enterrado. Entubado.",
}
INSTALL_OPEN = {"en": "Open Air", "fr": "À l'air libre", "es": "Al aire"}
INSTALL_CONDUIT = {
    "en": "In conduit",
    "fr": "En canalisation",
    "es": "Entubado",
}

REDUCED_HALOGENS = {
    "en": "Reduced halogens, Chlorine < 15%",
    "fr": "Halogènes réduits, Chlore < 15%",
    "es": "Halógenos reducidos, Cloro < 15%",
}

IMG_BASE = "https://www.topcable.com/wp-content/uploads/2025/07/"
IMG_BASE_11 = "https://www.topcable.com/wp-content/uploads/2025/11/"


# ============================================================
# CABLE 1: XTREM® DN-F 0,6/1 kV
# ============================================================
def cable_xtrem_dnf(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "Thermosetting rubber (flexible) according to UNE 21150",
            "fr": "Caoutchouc thermodurcissable (souple) selon UNE 21150",
            "es": "Goma termoestable (flexible) según UNE 21150",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "Thermosetting flexible rubber. Black colour",
            "fr": "Caoutchouc flexible thermodurcissable. Couleur noire",
            "es": "Goma flexible termoestable. Color negro",
        }[lang]),
        make_prop(lang, "rated_voltage", "0.6/1", "kV"),
        make_prop(lang, "max_temp", "90", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_250[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED_MOBILE_25[lang], "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "cpr", "Eca according to EN 50575" if lang == "en" else "Eca selon EN 50575" if lang == "fr" else "Eca según EN 50575"),
        make_prop(lang, "min_bending", {
            "en": "3x cable diameter < 12 mm, 4x cable diameter ≥ 12 mm",
            "fr": "3x diamètre du câble < 12 mm, 4x diamètre du câble ≥ 12 mm",
            "es": "3x diámetro del cable < 12 mm, 4x diámetro del cable ≥ 12 mm",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_EXCELLENT[lang]),
        make_prop(lang, "uv", UV_EN50618[lang]),
        make_prop(lang, "water", WATER_AD8[lang]),
        make_prop(lang, "installation", {
            "en": "Open Air. Submersible pumps cable",
            "fr": "À l'air libre. Câble pour pompes submersibles",
            "es": "Al aire. Cable para bombas sumergibles",
        }[lang]),
        make_prop(lang, "standards_ref", "UNE 21150"),
        make_prop(lang, "standards_approvals", "RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Industrial facilities, Transportable machines, Agricultural applications",
            "fr": "Installations industrielles, Machines transportables, Applications agricoles",
            "es": "Instalaciones industriales, Máquinas transportables, Aplicaciones agrícolas",
        }[lang]),
    ]

CABLE_1 = {
    "common": {
        "slug": "xtrem-dn-f",
        "mpn": "DN-F",
        "brand": "XTREM®",
        "family": "rubber",
        "datasheet_slug": "xtrem-dn-f",
        "images": [
            IMG_BASE + "topcable-dn-f-0-6-1-kv-flexible-rubber-cable-0-6-1kv-for-industrial-use-01.png",
            IMG_BASE + "TOPCABLE_XTREM_DN_F.webp",
            IMG_BASE + "bobina_negra.png"
        ],
    },
    "data": {
        "en": {
            "name": "XTREM® DN-F 0,6/1 kV",
            "description": "Flexible rubber cable 0,6/1 kV, for industrial use. ACCORDING TO: UNE 21150. XTREM® DN-F is a flexible rubber cable for heavy mobile duty. Suitable for installations in dry, damp or wet locations, outdoors, for hazardous areas with explosive gas atmospheres, machines in industrial workshops, motors and transportable machines; on construction sites and for agricultural exploitations. Suitable for submerged installations (AD8).",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_INDUSTRIAL["en"],
            "properties": cable_xtrem_dnf("en"),
        },
        "fr": {
            "name": "XTREM® DN-F 0,6/1 kV",
            "description": "Câble souple en caoutchouc 0,6/1 kV, pour usage industriel. SELON : UNE 21150. Le XTREM® DN-F est un câble souple en caoutchouc pour service mobile lourd. Adapté aux installations en milieux secs, humides ou mouillés, en extérieur, pour les zones dangereuses avec atmosphères explosives, machines dans les ateliers industriels, moteurs et machines transportables ; sur les chantiers et pour les exploitations agricoles. Adapté aux installations submersibles (AD8).",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_INDUSTRIAL["fr"],
            "properties": cable_xtrem_dnf("fr"),
        },
        "es": {
            "name": "XTREM® DN-F 0,6/1 kV",
            "description": "Cable flexible de goma 0,6/1 kV, para uso industrial. NORMAS DE REFERENCIA: UNE 21150. El XTREM® DN-F es un cable de goma flexible para servicio móvil pesado. Adecuado para instalaciones en ambientes secos, húmedos o mojados, en exteriores, para zonas peligrosas con atmósferas de gas explosivo, máquinas en talleres industriales, motores y máquinas transportables; en obras de construcción y explotaciones agrícolas. Apto para instalaciones sumergibles (AD8).",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_INDUSTRIAL["es"],
            "properties": cable_xtrem_dnf("es"),
        },
    },
}


# ============================================================
# CABLE 2: POWERFLEX® PLUS YMvKf
# ============================================================
def cable_powerflex_ymvkf(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "Cross-linked polyethylene type XLPE according to IEC 60502-1",
            "fr": "Polyéthylène réticulé type XLPE selon IEC 60502-1",
            "es": "Polietileno reticulado tipo XLPE según IEC 60502-1",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "PVC (flexible). Grey colour",
            "fr": "PVC (souple). Couleur grise",
            "es": "PVC (flexible). Color gris",
        }[lang]),
        make_prop(lang, "rated_voltage", "0.6/1", "kV"),
        make_prop(lang, "max_temp", "90", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_250[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED[lang], "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "fire_nonprop", FIRE_NONPROP_3_24[lang]),
        make_prop(lang, "cpr", {
            "en": "Cca-s2, d2, a3 according to EN 50575",
            "fr": "Cca-s2, d2, a3 selon EN 50575",
            "es": "Cca-s2, d2, a3 según EN 50575",
        }[lang]),
        make_prop(lang, "reduced_halogens", REDUCED_HALOGENS[lang]),
        make_prop(lang, "min_bending", {
            "en": "5x cable diameter",
            "fr": "5x diamètre du câble",
            "es": "5x diámetro del cable",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_ACCEPTABLE[lang]),
        make_prop(lang, "uv", UV_UNE211605[lang]),
        make_prop(lang, "water", WATER_AD7[lang]),
        make_prop(lang, "installation", INSTALL_FULL[lang]),
        make_prop(lang, "standards_ref", "IEC 60502-1, HD 604-4-D"),
        make_prop(lang, "standards_approvals", "KEMA-KEUR, BUREAU VERITAS, AENOR, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Industrial facilities, Construction sites, Power distribution",
            "fr": "Installations industrielles, Chantiers de construction, Distribution d'énergie",
            "es": "Instalaciones industriales, Obras de construcción, Distribución de energía",
        }[lang]),
    ]

CABLE_2 = {
    "common": {
        "slug": "powerflex-plus-ymvkf",
        "mpn": "YMvKf",
        "brand": "POWERFLEX®",
        "family": "power",
        "datasheet_slug": "powerflex-plus-ymvkf",
        "images": [
            IMG_BASE + "topcable-ymvkf-the-universal-cable-for-power-transmission-with-improved-fire-proof-properties-01.png",
            IMG_BASE + "TOPCABLE_POWERFLEX_PLUS_YMvKf.webp",
            IMG_BASE + "bobina_gris.png"
        ],
        "languages": ["en", "fr"],
    },
    "data": {
        "en": {
            "name": "POWERFLEX® PLUS YMvKf",
            "description": "The universal cable for power transmission with improved fire proof properties. ACCORDING TO: IEC 60502-1 / HD 604-4-D. POWERFLEX® PLUS YMvKf is a fire retardant cable recommended for public places and hazardous industries. Suitable for industrial low voltage connections, urban grids, and building installations with enhanced flexibility for difficult layouts. Can be used in buried installations, tubes, or outdoors without additional protection, withstanding damp conditions and water immersion (AD7).",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_INDUSTRIAL["en"],
            "properties": cable_powerflex_ymvkf("en"),
        },
        "fr": {
            "name": "POWERFLEX® PLUS YMvKf",
            "description": "Le câble universel pour la transmission d'énergie avec des propriétés anti-feu améliorées. SELON : IEC 60502-1 / HD 604-4-D. Le POWERFLEX® PLUS YMvKf est un câble ignifuge recommandé pour les lieux publics et les industries à risque. Adapté aux connexions industrielles basse tension, réseaux urbains et installations de bâtiments avec une flexibilité améliorée pour les configurations difficiles. Peut être utilisé en installations enterrées, en tubes ou en extérieur sans protection supplémentaire, résistant aux conditions humides et à l'immersion (AD7).",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_INDUSTRIAL["fr"],
            "properties": cable_powerflex_ymvkf("fr"),
        },
    },
}


# ============================================================
# CABLE 3: POWERFLEX® PLUS YMvKf 1,8/3 kV
# ============================================================
def cable_powerflex_ymvkf_18(lang):
    props = cable_powerflex_ymvkf(lang)
    # Replace voltage
    for p in props:
        if p["name"] == PROP_NAMES[lang]["rated_voltage"]:
            p["value"] = "1.8/3"
    # Replace outer sheath to include grey or black
    for p in props:
        if p["name"] == PROP_NAMES[lang]["outer_sheath"]:
            p["value"] = {
                "en": "PVC (flexible). Grey or black colour",
                "fr": "PVC (souple). Couleur grise ou noire",
                "es": "PVC (flexible). Color gris o negro",
            }[lang]
    return props

CABLE_3 = {
    "common": {
        "slug": "powerflex-plus-ymvkf-18-3kv",
        "mpn": "YMvKf 1,8/3 kV",
        "brand": "POWERFLEX®",
        "family": "power",
        "datasheet_slug": "powerflex-plus-ymvkf-18-3kv",
        "images": [
            IMG_BASE + "topcable-ymvkf-1-8-3kv-the-universal-1-8-3kv-cable-for-power-transmission-with-improved-fire-proof-properties-01.png",
            IMG_BASE + "TOPCABLE_POWERFLEX_PLUS_YMvKf-1.webp",
            IMG_BASE + "bobina_gris.png"
        ],
        "languages": ["en", "fr"],
    },
    "data": {
        "en": {
            "name": "POWERFLEX® PLUS YMvKf 1,8/3 kV",
            "description": "The universal 1,8/3 kV cable for power transmission with improved fire proof properties. ACCORDING TO: IEC 60502-1 / HD 604-4-D. POWERFLEX® PLUS YMvKf 1,8/3 kV is a fire retardant cable recommended for public places and hazardous industries with flexibility suitable for difficult layouts.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_INDUSTRIAL["en"],
            "properties": cable_powerflex_ymvkf_18("en"),
        },
        "fr": {
            "name": "POWERFLEX® PLUS YMvKf 1,8/3 kV",
            "description": "Le câble universel 1,8/3 kV pour la transmission d'énergie avec des propriétés anti-feu améliorées. SELON : IEC 60502-1 / HD 604-4-D. Le POWERFLEX® PLUS YMvKf 1,8/3 kV est un câble ignifuge recommandé pour les lieux publics et les industries à risque avec une flexibilité adaptée aux configurations difficiles.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_INDUSTRIAL["fr"],
            "properties": cable_powerflex_ymvkf_18("fr"),
        },
    },
}


# ============================================================
# CABLE 4: TOXFREE® LSZH RZ1-K 1,8/3 kV
# ============================================================
def cable_rz1k_18(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "Cross-linked polyethylene type XLPE according to IEC 60502-1",
            "fr": "Polyéthylène réticulé type XLPE selon IEC 60502-1",
            "es": "Polietileno reticulado tipo XLPE según IEC 60502-1",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "Low smoke halogen free polyolefin. Green colour",
            "fr": "Polyoléfine sans halogène à faible émission de fumée. Couleur verte",
            "es": "Poliolefina libre de halógenos y baja emisión de humo. Color verde",
        }[lang]),
        make_prop(lang, "rated_voltage", "1.8/3", "kV"),
        make_prop(lang, "max_temp", "90", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_250[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED[lang], "°C"),
        make_prop(lang, "min_install_temp", "0", "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "fire_nonprop", FIRE_NONPROP[lang]),
        make_prop(lang, "cpr", {
            "en": "B2ca-s1a, d1, a1 or Cca-s1a, d1, a1 (according to cross-section) according to EN 50575",
            "fr": "B2ca-s1a, d1, a1 ou Cca-s1a, d1, a1 (selon la section) selon EN 50575",
            "es": "B2ca-s1a, d1, a1 o Cca-s1a, d1, a1 (según la sección) según EN 50575",
        }[lang]),
        make_prop(lang, "halogen_free", HALOGEN_FREE[lang]),
        make_prop(lang, "low_corrosive_gases", LOW_CORROSIVE_GASES[lang]),
        make_prop(lang, "low_smoke", LOW_SMOKE_61034[lang]),
        make_prop(lang, "light_transmittance", "> 80%"),
        make_prop(lang, "min_bending", {
            "en": "5x cable diameter",
            "fr": "5x diamètre du câble",
            "es": "5x diámetro del cable",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_ACCEPTABLE[lang]),
        make_prop(lang, "uv", UV_EN50618[lang]),
        make_prop(lang, "water", WATER_AD8[lang]),
        make_prop(lang, "installation", INSTALL_FULL[lang]),
        make_prop(lang, "standards_ref", "IEC 60502-1"),
        make_prop(lang, "standards_approvals", "RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Industrial facilities, Construction sites, Power distribution",
            "fr": "Installations industrielles, Chantiers de construction, Distribution d'énergie",
            "es": "Instalaciones industriales, Obras de construcción, Distribución de energía",
        }[lang]),
    ]

CABLE_4 = {
    "common": {
        "slug": "toxfree-lszh-rz1-k-18-3kv",
        "mpn": "RZ1-K 1,8/3 kV",
        "brand": "TOXFREE®",
        "family": "lszh",
        "datasheet_slug": "toxfree-lszh-rz1-k-18-3kv",
        "images": [
            IMG_BASE + "topcable-rz1-k-1-8-3kv-flexible-lszh-power-1-8-3kv-cable-for-public-places-01.png",
            IMG_BASE + "TOPCABLE_TOXFREE_ZH_RZ1_K.webp",
            IMG_BASE + "bobina_verde.png"
        ],
    },
    "data": {
        "en": {
            "name": "TOXFREE® LSZH RZ1-K 1,8/3 kV",
            "description": "Flexible LSZH power 1,8/3 kV cable, for public places. ACCORDING TO: IEC 60502-1. TOXFREE® LSZH RZ1-K 1,8/3 kV is a LSZH safety cable. In the event of fire, it does not emit toxic gases, nor does it give off corrosive gases, avoiding any possible damage to people or electronic equipment. Highly recommended for use in public places such as: hospitals, schools, museums, airports, bus terminals, shopping centres, offices, and laboratories.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_LSZH["en"],
            "properties": cable_rz1k_18("en"),
        },
        "fr": {
            "name": "TOXFREE® LSZH RZ1-K 1,8/3 kV",
            "description": "Câble d'alimentation LSZH souple 1,8/3 kV pour les lieux publics. SELON : IEC 60502-1. Le TOXFREE® LSZH RZ1-K 1,8/3 kV est un câble de sécurité LSZH. En cas d'incendie, il n'émet pas de gaz toxiques ni de gaz corrosifs, évitant tout dommage possible aux personnes ou aux équipements électroniques. Fortement recommandé pour les lieux publics tels que : hôpitaux, écoles, musées, aéroports, gares routières, centres commerciaux, bureaux et laboratoires.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_LSZH["fr"],
            "properties": cable_rz1k_18("fr"),
        },
        "es": {
            "name": "TOXFREE® LSZH RZ1-K 1,8/3 kV",
            "description": "Cable 1,8/3 kV de potencia flexible LSZH para locales de pública concurrencia. NORMAS DE REFERENCIA: IEC 60502-1. El TOXFREE® LSZH RZ1-K 1,8/3 kV es un cable de seguridad LSZH. En caso de incendio, no emite gases tóxicos ni corrosivos, evitando cualquier daño posible a las personas o equipos electrónicos. Muy recomendado para locales de pública concurrencia tales como: hospitales, escuelas, museos, aeropuertos, terminales de autobuses, centros comerciales, oficinas y laboratorios.",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_LSZH["es"],
            "properties": cable_rz1k_18("es"),
        },
    },
}


# ============================================================
# CABLE 5: TOXFREE® ULTRA TXXI
# ============================================================
def cable_txxi(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "Flexible cross-linked polyethylene type XLPE according to IEC 60502-1",
            "fr": "Polyéthylène réticulé flexible type XLPE selon IEC 60502-1",
            "es": "Polietileno reticulado flexible tipo XLPE según IEC 60502-1",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "Low smoke halogen free polyolefin, type ST8 according to IEC 60502-1. Black colour",
            "fr": "Polyoléfine sans halogène à faible émission de fumée, type ST8 selon IEC 60502-1. Couleur noire",
            "es": "Poliolefina libre de halógenos y baja emisión de humo, tipo ST8 según IEC 60502-1. Color negro",
        }[lang]),
        make_prop(lang, "rated_voltage", "0.6/1", "kV"),
        make_prop(lang, "max_temp", "90", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_250[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED[lang], "°C"),
        make_prop(lang, "min_install_temp", "0", "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "fire_nonprop", {
            "en": "Fire non-propagation according to EN 50399",
            "fr": "Non-propagation de l'incendie selon EN 50399",
            "es": "No propagación del incendio según EN 50399",
        }[lang]),
        make_prop(lang, "cpr", {
            "en": "Dca-s1, d2, a1 according to EN 50575",
            "fr": "Dca-s1, d2, a1 selon EN 50575",
            "es": "Dca-s1, d2, a1 según EN 50575",
        }[lang]),
        make_prop(lang, "halogen_free", HALOGEN_FREE[lang]),
        make_prop(lang, "low_corrosive_gases", LOW_CORROSIVE_GASES[lang]),
        make_prop(lang, "min_bending", {
            "en": "5x cable diameter",
            "fr": "5x diamètre du câble",
            "es": "5x diámetro del cable",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_ACCEPTABLE[lang]),
        make_prop(lang, "uv", UV_EN50618[lang]),
        make_prop(lang, "water", WATER_AD8[lang]),
        make_prop(lang, "installation", INSTALL_FULL[lang]),
        make_prop(lang, "standards_ref", "IEC 60502-1"),
        make_prop(lang, "standards_approvals", "RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Fixed installations, Compact spaces, Power distribution",
            "fr": "Installations fixes, Espaces compacts, Distribution d'énergie",
            "es": "Instalaciones fijas, Espacios compactos, Distribución de energía",
        }[lang]),
    ]

CABLE_5 = {
    "common": {
        "slug": "toxfree-ultra-txxi",
        "mpn": "TXXI",
        "brand": "TOXFREE®",
        "family": "lszh",
        "datasheet_slug": "toxfree-ultra-txxi",
        "images": [
            IMG_BASE_11 + "topcable-ultra-txxi.png",
            IMG_BASE + "bobina_negra.png"
        ],
        "languages": ["en", "fr"],
    },
    "data": {
        "en": {
            "name": "TOXFREE® ULTRA TXXI",
            "description": "Extra flexible low smoke halogen free cable for fixed installations. ACCORDING TO: IEC 60502-1. TOXFREE® ULTRA TXXI is suitable for installations where an enhanced flexibility is needed to aid swift installation into compact and restricted spaces.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_LSZH["en"],
            "properties": cable_txxi("en"),
        },
        "fr": {
            "name": "TOXFREE® ULTRA TXXI",
            "description": "Câble d'alimentation LSHF extra-flexible pour installations fixes. SELON : IEC 60502-1. Le TOXFREE® ULTRA TXXI est adapté aux installations nécessitant une flexibilité accrue pour faciliter une installation rapide dans des espaces compacts et restreints.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_LSZH["fr"],
            "properties": cable_txxi("fr"),
        },
    },
}


# ============================================================
# CABLE 6: TOXFREE® LSZH FR-N1X1G1 Flex 1,8/3 kV
# ============================================================
def cable_n1x1g1_18(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "Cross-linked polyethylene type XLPE according to IEC 60502-1",
            "fr": "Polyéthylène réticulé type XLPE selon IEC 60502-1",
            "es": "Polietileno reticulado tipo XLPE según IEC 60502-1",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "Low smoke halogen free polyolefin. Green colour",
            "fr": "Polyoléfine sans halogène à faible émission de fumée. Couleur verte",
            "es": "Poliolefina libre de halógenos y baja emisión de humo. Color verde",
        }[lang]),
        make_prop(lang, "rated_voltage", "1.8/3", "kV"),
        make_prop(lang, "max_temp", "90", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_250[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED[lang], "°C"),
        make_prop(lang, "min_install_temp", "0", "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "fire_nonprop", FIRE_NONPROP[lang]),
        make_prop(lang, "cpr", {
            "en": "B2ca-s1a, d1, a1 or Cca-s1a, d1, a1 (according to cross-section) according to EN 50575",
            "fr": "B2ca-s1a, d1, a1 ou Cca-s1a, d1, a1 (selon la section) selon EN 50575",
            "es": "B2ca-s1a, d1, a1 o Cca-s1a, d1, a1 (según la sección) según EN 50575",
        }[lang]),
        make_prop(lang, "halogen_free", HALOGEN_FREE[lang]),
        make_prop(lang, "low_corrosive_gases", LOW_CORROSIVE_GASES[lang]),
        make_prop(lang, "low_smoke", LOW_SMOKE_61034[lang]),
        make_prop(lang, "light_transmittance", "> 80%"),
        make_prop(lang, "min_bending", {
            "en": "5x cable diameter",
            "fr": "5x diamètre du câble",
            "es": "5x diámetro del cable",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_ACCEPTABLE[lang]),
        make_prop(lang, "uv", UV_EN50618[lang]),
        make_prop(lang, "water", WATER_AD8[lang]),
        make_prop(lang, "installation", INSTALL_FULL[lang]),
        make_prop(lang, "standards_ref", "IEC 60502-1, NF C 32-323"),
        make_prop(lang, "standards_approvals", "SEC, KEMA-KEUR, AENOR, UKCA, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "High-occupancy buildings (ERP & IGH), Industrial facilities, Data centres",
            "fr": "Bâtiments à forte occupation (ERP et IGH), Installations industrielles, Centres de données",
            "es": "Edificios de alta ocupación (ERP e IGH), Instalaciones industriales, Centros de datos",
        }[lang]),
    ]

CABLE_6 = {
    "common": {
        "slug": "toxfree-lszh-fr-n1x1g1-flex-18-3kv",
        "mpn": "FR-N1X1G1 Flex 1,8/3 kV",
        "brand": "TOXFREE®",
        "family": "lszh",
        "datasheet_slug": "toxfree-lszh-fr-n1x1g1-flex-18-3kv",
        "images": [
            IMG_BASE + "topcable-fr-n1x1g1-flex-flexible-lszh-power-cable-for-public-places-erp-and-igh-01.png",
            IMG_BASE + "bobina_verde.png"
        ],
        "languages": ["en", "fr"],
    },
    "data": {
        "en": {
            "name": "TOXFREE® LSZH FR-N1X1G1 Flex 1,8/3 kV",
            "description": "Flexible LSZH power cable 1,8/3 kV for public places and high-rise buildings (ERP & IGH). BASED ON: NF C 32-323. ACCORDING TO: IEC 60502-1. TOXFREE® LSZH FR-N1X1G1 Flex 1,8/3 kV is a LSZH safety cable. In the event of fire, it does not emit toxic gases, nor does it give off corrosive gases, avoiding any possible damage to people or electronic equipment. Highly recommended for use in public places such as: hospitals, schools, museums, airports, bus terminals, shopping centres, offices, and laboratories.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_LSZH["en"],
            "properties": cable_n1x1g1_18("en"),
        },
        "fr": {
            "name": "TOXFREE® LSZH FR-N1X1G1 Flex 1,8/3 kV",
            "description": "Câble d'alimentation LSZH souple 1,8/3 kV pour les lieux publics et immeubles de grande hauteur (ERP et IGH). BASÉ SUR : NF C 32-323. SELON : IEC 60502-1. Le TOXFREE® LSZH FR-N1X1G1 Flex 1,8/3 kV est un câble de sécurité LSZH. En cas d'incendie, il n'émet pas de gaz toxiques ni de gaz corrosifs, évitant tout dommage possible aux personnes ou aux équipements électroniques. Fortement recommandé pour les lieux publics tels que : hôpitaux, écoles, musées, aéroports, gares routières, centres commerciaux, bureaux et laboratoires.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_LSZH["fr"],
            "properties": cable_n1x1g1_18("fr"),
        },
    },
}


# ============================================================
# CABLE 7: TOXFREE® LSZH RZ1MZ1-K
# ============================================================
def cable_rz1mz1k(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "Cross-linked polyethylene type XLPE according to IEC 60502-1",
            "fr": "Polyéthylène réticulé type XLPE selon IEC 60502-1",
            "es": "Polietileno reticulado tipo XLPE según IEC 60502-1",
        }[lang]),
        make_prop(lang, "separation_sheath", {
            "en": "Low smoke halogen free polyolefin",
            "fr": "Polyoléfine sans halogène à faible émission de fumée",
            "es": "Poliolefina libre de halógenos y baja emisión de humo",
        }[lang]),
        make_prop(lang, "armour", {
            "en": "Galvanized steel wire (multiconductor) or aluminium wire (single-conductor, to prevent parasitic currents)",
            "fr": "Fil d'acier galvanisé (multiconducteur) ou fil d'aluminium (monoconducteur, pour éviter les courants parasites)",
            "es": "Hilo de acero galvanizado (multiconductor) o hilo de aluminio (monoconductor, para evitar corrientes parásitas)",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "Low smoke halogen free polyolefin. Black colour",
            "fr": "Polyoléfine sans halogène à faible émission de fumée. Couleur noire",
            "es": "Poliolefina libre de halógenos y baja emisión de humo. Color negro",
        }[lang]),
        make_prop(lang, "rated_voltage", "0.6/1", "kV"),
        make_prop(lang, "max_temp", "90", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_250[lang], "°C"),
        make_prop(lang, "min_service_temp", "-50", "°C"),
        make_prop(lang, "min_install_temp", "0", "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "cpr", {
            "en": "Cca-s1b, d1, a2 according to EN 50575",
            "fr": "Cca-s1b, d1, a2 selon EN 50575",
            "es": "Cca-s1b, d1, a2 según EN 50575",
        }[lang]),
        make_prop(lang, "halogen_free", HALOGEN_FREE[lang]),
        make_prop(lang, "low_corrosive_gases", LOW_CORROSIVE_GASES[lang]),
        make_prop(lang, "low_smoke", LOW_SMOKE_61034[lang]),
        make_prop(lang, "light_transmittance", "> 60%"),
        make_prop(lang, "min_bending", {
            "en": "10x cable diameter",
            "fr": "10x diamètre du câble",
            "es": "10x diámetro del cable",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG4[lang]),
        make_prop(lang, "rodent_proof", {
            "en": "Rodent proof",
            "fr": "Anti-rongeurs",
            "es": "Anti-roedores",
        }[lang]),
        make_prop(lang, "chemical_oil", CHEM_GOOD[lang]),
        make_prop(lang, "uv", UV_EN50618[lang]),
        make_prop(lang, "hydrocarbon", {
            "en": "Hydrocarbon resistant",
            "fr": "Résistant aux hydrocarbures",
            "es": "Resistente a los hidrocarburos",
        }[lang]),
        make_prop(lang, "water", WATER_AD5[lang]),
        make_prop(lang, "atex", {
            "en": "Suitable for ATEX explosive atmospheres according to ITC-BT 29",
            "fr": "Adapté aux atmosphères explosives ATEX selon ITC-BT 29",
            "es": "Apto para atmósferas explosivas ATEX según ITC-BT 29",
        }[lang]),
        make_prop(lang, "installation", INSTALL_FULL[lang]),
        make_prop(lang, "standards_ref", "IEC 60502-1"),
        make_prop(lang, "standards_approvals", "AENOR, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Industrial facilities, ATEX zones, Power distribution",
            "fr": "Installations industrielles, Zones ATEX, Distribution d'énergie",
            "es": "Instalaciones industriales, Zonas ATEX, Distribución de energía",
        }[lang]),
    ]

CABLE_7 = {
    "common": {
        "slug": "toxfree-lszh-rz1mz1-k",
        "mpn": "RZ1MZ1-K",
        "brand": "TOXFREE®",
        "family": "lszh",
        "datasheet_slug": "toxfree-lszh-rz1mz1-k",
        "images": [
            IMG_BASE + "topcable-rz1mz1-k-lszh-armoured-cable-with-galvanized-steel-wire-armour-atex-01.png",
            IMG_BASE + "TOPCABLE_TOXFREE_ZH_RZ1MZ1_K.webp",
            IMG_BASE + "bobina_negra.png"
        ],
    },
    "data": {
        "en": {
            "name": "TOXFREE® LSZH RZ1MZ1-K",
            "description": "LSZH armoured cable with galvanized steel wire armour (ATEX). ACCORDING TO: IEC 60502-1. TOXFREE® LSZH RZ1MZ1-K is a LSZH armoured cable. In the event of fire, it does not emit toxic gases, nor does it give off corrosive gases, avoiding any possible damage to people or electronic equipment. Recommended for industrial installations requiring severe mechanical protection, long-distance runs, and areas with fire and explosion risks (ATEX).",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_INDUSTRIAL["en"],
            "properties": cable_rz1mz1k("en"),
        },
        "fr": {
            "name": "TOXFREE® LSZH RZ1MZ1-K",
            "description": "Câble armé LSZH avec armure en fils d'acier galvanisé (ATEX). SELON : IEC 60502-1. Le TOXFREE® LSZH RZ1MZ1-K est un câble armé LSZH. En cas d'incendie, il n'émet pas de gaz toxiques ni de gaz corrosifs, évitant tout dommage possible aux personnes ou aux équipements électroniques. Recommandé pour les installations industrielles nécessitant une protection mécanique sévère, les longues distances et les zones à risques d'incendie et d'explosion (ATEX).",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_INDUSTRIAL["fr"],
            "properties": cable_rz1mz1k("fr"),
        },
        "es": {
            "name": "TOXFREE® LSZH RZ1MZ1-K",
            "description": "Cable armado LSZH con armadura de hilos de acero galvanizado (ATEX). NORMAS DE REFERENCIA: IEC 60502-1. El TOXFREE® LSZH RZ1MZ1-K es un cable armado LSZH. En caso de incendio, no emite gases tóxicos ni corrosivos, evitando cualquier daño posible a las personas o equipos electrónicos. Recomendado para instalaciones industriales que requieren protección mecánica severa, largas distancias y zonas con riesgo de incendio y explosión (ATEX).",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_INDUSTRIAL["es"],
            "properties": cable_rz1mz1k("es"),
        },
    },
}


# ============================================================
# CABLE 8: TOXFREE® LSZH XZ1 AL
# ============================================================
def cable_xz1_al(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_ALUMINIUM_CL2[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "Cross-linked polyethylene type XLPE according to UNE-HD 603-5x",
            "fr": "Polyéthylène réticulé type XLPE selon UNE-HD 603-5x",
            "es": "Polietileno reticulado tipo XLPE según UNE-HD 603-5x",
        }[lang]),
        make_prop(lang, "screen", {
            "en": "Overlapping aluminium-polyester tape with 100% coverage plus tinned copper drain wire",
            "fr": "Bande aluminium-polyester chevauchante avec couverture 100% et fil de drainage en cuivre étamé",
            "es": "Cinta aluminio-poliéster solapada con cobertura 100% y hilo de drenaje de cobre estañado",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "Low smoke halogen free polyolefin. Black colour",
            "fr": "Polyoléfine sans halogène à faible émission de fumée. Couleur noire",
            "es": "Poliolefina libre de halógenos y baja emisión de humo. Color negro",
        }[lang]),
        make_prop(lang, "rated_voltage", "0.6/1 (1.2)", "kV"),
        make_prop(lang, "max_temp", "90", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_250[lang], "°C"),
        make_prop(lang, "min_service_temp", "-25", "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "cpr", {
            "en": "Eca according to EN 50575",
            "fr": "Eca selon EN 50575",
            "es": "Eca según EN 50575",
        }[lang]),
        make_prop(lang, "halogen_free", HALOGEN_FREE[lang]),
        make_prop(lang, "low_corrosive_gases", LOW_CORROSIVE_GASES[lang]),
        make_prop(lang, "min_bending", {
            "en": "15x cable diameter",
            "fr": "15x diamètre du câble",
            "es": "15x diámetro del cable",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_ACCEPTABLE[lang]),
        make_prop(lang, "uv", UV_HD603[lang]),
        make_prop(lang, "installation", INSTALL_FULL[lang]),
        make_prop(lang, "standards_ref", "UNE-HD 603-5x"),
        make_prop(lang, "standards_approvals", "AENOR, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Power distribution, Industrial facilities, Buried PV installations",
            "fr": "Distribution d'énergie, Installations industrielles, Installations photovoltaïques enterrées",
            "es": "Distribución de energía, Instalaciones industriales, Instalaciones fotovoltaicas enterradas",
        }[lang]),
    ]

CABLE_8 = {
    "common": {
        "slug": "toxfree-lszh-xz1-al",
        "mpn": "XZ1 AL",
        "brand": "TOXFREE®",
        "family": "lszh",
        "datasheet_slug": "toxfree-lszh-xz1-al",
        "images": [
            IMG_BASE + "topcable-xz1-al-screened-lszh-safety-cable-01.png",
            IMG_BASE + "TOPCABLE_TOXFREE_ZH_XZ1_AL.webp",
            IMG_BASE + "bobina_negra.png"
        ],
    },
    "data": {
        "en": {
            "name": "TOXFREE® LSZH XZ1 AL",
            "description": "Screened LSZH power cable with aluminium conductor. ACCORDING TO: UNE-HD 603-5x. TOXFREE® LSZH XZ1 AL is a screened LSZH safety cable. In the event of fire, it does not emit toxic gases, nor does it give off corrosive gases, avoiding any possible damage to people or electronic equipment. Designed for fixed installations in public low-voltage distribution networks, suitable for industrial, solar photovoltaic and power distribution applications.",
            "material": MATERIAL_ALUMINIUM_CL2["en"],
            "audience": AUDIENCE_LSZH["en"],
            "properties": cable_xz1_al("en"),
        },
        "fr": {
            "name": "TOXFREE® LSZH XZ1 AL",
            "description": "Câble d'alimentation LSZH blindé avec conducteur en aluminium. SELON : UNE-HD 603-5x. Le TOXFREE® LSZH XZ1 AL est un câble de sécurité LSZH blindé. En cas d'incendie, il n'émet pas de gaz toxiques ni de gaz corrosifs, évitant tout dommage possible aux personnes ou aux équipements électroniques. Conçu pour les installations fixes dans les réseaux de distribution publique basse tension, adapté aux applications industrielles, photovoltaïques et de distribution d'énergie.",
            "material": MATERIAL_ALUMINIUM_CL2["fr"],
            "audience": AUDIENCE_LSZH["fr"],
            "properties": cable_xz1_al("fr"),
        },
        "es": {
            "name": "TOXFREE® LSZH XZ1 AL",
            "description": "Cable de potencia apantallado LSZH con conductor de aluminio. NORMAS DE REFERENCIA: UNE-HD 603-5x. El TOXFREE® LSZH XZ1 AL es un cable de seguridad LSZH apantallado. En caso de incendio, no emite gases tóxicos ni corrosivos, evitando cualquier daño posible a las personas o equipos electrónicos. Diseñado para instalaciones fijas en redes de distribución pública de baja tensión, apto para aplicaciones industriales, fotovoltaicas y de distribución de energía.",
            "material": MATERIAL_ALUMINIUM_CL2["es"],
            "audience": AUDIENCE_LSZH["es"],
            "properties": cable_xz1_al("es"),
        },
    },
}


# ============================================================
# CABLE 9: FLEXTEL® 110 ES05VV-F
# ============================================================
def cable_flextel_110(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "PVC (flexible) according to UNE 21031",
            "fr": "PVC (souple) selon UNE 21031",
            "es": "PVC (flexible) según UNE 21031",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "PVC (flexible). Grey or black colour",
            "fr": "PVC (souple). Couleur grise ou noire",
            "es": "PVC (flexible). Color gris o negro",
        }[lang]),
        make_prop(lang, "rated_voltage", "300/500", "V"),
        make_prop(lang, "max_temp", "70", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_160[lang], "°C"),
        make_prop(lang, "min_service_temp", {
            "en": "-30 (fixed installations) and 0 (mobile use)",
            "fr": "-30 (installations fixes) et 0 (service mobile)",
            "es": "-30 (instalaciones fijas) y 0 (servicio móvil)",
        }[lang], "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "cpr", {
            "en": "Eca according to EN 50575",
            "fr": "Eca selon EN 50575",
            "es": "Eca según EN 50575",
        }[lang]),
        make_prop(lang, "reduced_halogens", REDUCED_HALOGENS[lang]),
        make_prop(lang, "min_bending", {
            "en": "5x cable diameter",
            "fr": "5x diamètre du câble",
            "es": "5x diámetro del cable",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_GOOD[lang]),
        make_prop(lang, "uv", UV_UNE211605[lang]),
        make_prop(lang, "water", WATER_AD5[lang]),
        make_prop(lang, "installation", INSTALL_FULL[lang]),
        make_prop(lang, "standards_ref", "UNE 21031"),
        make_prop(lang, "standards_approvals", "RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Machinery connection, Mobile service, Industrial control",
            "fr": "Raccordement de machines, Service mobile, Contrôle industriel",
            "es": "Conexión de maquinaria, Servicio móvil, Control industrial",
        }[lang]),
    ]

CABLE_9 = {
    "common": {
        "slug": "flextel-110-es05vv-f",
        "mpn": "ES05VV-F",
        "brand": "FLEXTEL®",
        "family": "pvc",
        "datasheet_slug": "flextel-110-es05vv-f",
        "images": [
            IMG_BASE + "topcable-es05vv-f-flexible-multi-conductor-control-cable-for-mobile-use-01.png",
            IMG_BASE + "TOPCABLE_FLEXTEL_110_ES05VV_F.webp",
            IMG_BASE + "bobina_gris.png"
        ],
    },
    "data": {
        "en": {
            "name": "FLEXTEL® 110 ES05VV-F",
            "description": "Flexible multi-conductor control cable for mobile use. ACCORDING TO: UNE 21031. FLEXTEL® 110 ES05VV-F is a flexible control cable, specially designed for the interconnection of machine parts and mobile service applications. Its flexibility facilitates installation and withstands continuous movement in industrial environments.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_INDUSTRIAL["en"],
            "properties": cable_flextel_110("en"),
        },
        "fr": {
            "name": "FLEXTEL® 110 ES05VV-F",
            "description": "Câble de contrôle souple multiconducteur pour service mobile. SELON : UNE 21031. Le FLEXTEL® 110 ES05VV-F est un câble de contrôle souple, spécialement conçu pour l'interconnexion de pièces de machines et les applications de service mobile. Sa flexibilité facilite l'installation et résiste aux mouvements continus dans les environnements industriels.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_INDUSTRIAL["fr"],
            "properties": cable_flextel_110("fr"),
        },
        "es": {
            "name": "FLEXTEL® 110 ES05VV-F",
            "description": "Cable de control flexible multiconductor para servicio móvil. NORMAS DE REFERENCIA: UNE 21031. El FLEXTEL® 110 ES05VV-F es un cable de control flexible, especialmente diseñado para la interconexión de partes de máquinas y aplicaciones de servicio móvil. Su flexibilidad facilita la instalación y resiste el movimiento continuo en entornos industriales.",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_INDUSTRIAL["es"],
            "properties": cable_flextel_110("es"),
        },
    },
}


# ============================================================
# CABLE 10: TOPFLEX® VV-F H05VV-F
# ============================================================
def cable_topflex_vvf(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "PVC (flexible) according to EN 50525-2-11",
            "fr": "PVC (souple) selon EN 50525-2-11",
            "es": "PVC (flexible) según EN 50525-2-11",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "PVC (flexible). Grey, white or black colour",
            "fr": "PVC (souple). Couleur grise, blanche ou noire",
            "es": "PVC (flexible). Color gris, blanco o negro",
        }[lang]),
        make_prop(lang, "rated_voltage", "300/500", "V"),
        make_prop(lang, "max_temp", "70", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_160[lang], "°C"),
        make_prop(lang, "min_service_temp", "5", "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "cpr", {
            "en": "Eca according to EN 50575",
            "fr": "Eca selon EN 50575",
            "es": "Eca según EN 50575",
        }[lang]),
        make_prop(lang, "reduced_halogens", REDUCED_HALOGENS[lang]),
        make_prop(lang, "min_bending", {
            "en": "3x cable diameter < 12 mm, 4x cable diameter ≥ 12 mm",
            "fr": "3x diamètre du câble < 12 mm, 4x diamètre du câble ≥ 12 mm",
            "es": "3x diámetro del cable < 12 mm, 4x diámetro del cable ≥ 12 mm",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_GOOD[lang]),
        make_prop(lang, "water", WATER_AD5[lang]),
        make_prop(lang, "installation", INSTALL_FULL[lang]),
        make_prop(lang, "standards_ref", "EN 50525-2-11, IEC 60227"),
        make_prop(lang, "standards_approvals", "SEC, HAR, AENOR, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Small household appliances, Household installations, Light mobile service",
            "fr": "Petits appareils électroménagers, Installations domestiques, Service mobile léger",
            "es": "Pequeños electrodomésticos, Instalaciones domésticas, Servicio móvil ligero",
        }[lang]),
    ]

CABLE_10 = {
    "common": {
        "slug": "topflex-vv-f-h05vv-f",
        "mpn": "H05VV-F",
        "brand": "TOPFLEX®",
        "family": "pvc",
        "datasheet_slug": "topflex-vv-f-h05vv-f",
        "images": [
            IMG_BASE + "topcable-h05vv-f-flexible-cable-for-connecting-small-electrical-appliances-01.png",
            IMG_BASE + "TOPCABLE_TOPFLEX_VV_F_H05VV_F.webp",
            IMG_BASE + "bobina_gris.png"
        ],
    },
    "data": {
        "en": {
            "name": "TOPFLEX® VV-F H05VV-F",
            "description": "Flexible cable for connecting small electrical appliances. ACCORDING TO: EN 50525-2-11 / IEC 60227. TOPFLEX® VV-F H05VV-F is specially designed for the connection of small household appliances such as vacuum cleaners, washing machines and refrigerators. Also suitable for household installations, light mobile service, furniture, wall partitions and prefabricated building elements.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_DOMESTIC["en"],
            "properties": cable_topflex_vvf("en"),
        },
        "fr": {
            "name": "TOPFLEX® VV-F H05VV-F",
            "description": "Câble souple pour connecter de petits appareils électriques. SELON : EN 50525-2-11 / IEC 60227. Le TOPFLEX® VV-F H05VV-F est spécialement conçu pour le raccordement de petits appareils électroménagers tels que aspirateurs, machines à laver et réfrigérateurs. Également adapté aux installations domestiques, service mobile léger, meubles, cloisons et éléments de construction préfabriqués.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_DOMESTIC["fr"],
            "properties": cable_topflex_vvf("fr"),
        },
        "es": {
            "name": "TOPFLEX® VV-F H05VV-F",
            "description": "Cable flexible para conectar pequeños electrodomésticos. NORMAS DE REFERENCIA: EN 50525-2-11 / IEC 60227. El TOPFLEX® VV-F H05VV-F está especialmente diseñado para la conexión de pequeños electrodomésticos como aspiradoras, lavadoras y frigoríficos. También apto para instalaciones domésticas, servicio móvil ligero, muebles, tabiques y elementos de construcción prefabricados.",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_DOMESTIC["es"],
            "properties": cable_topflex_vvf("es"),
        },
    },
}


# ============================================================
# MAIN: Generate all files
# ============================================================

ALL_CABLES = [CABLE_1, CABLE_2, CABLE_3, CABLE_4, CABLE_5, CABLE_6, CABLE_7, CABLE_8, CABLE_9, CABLE_10]

def main():
    count = 0
    for cable in ALL_CABLES:
        languages = cable["common"].get("languages", ["en", "fr", "es"])
        for lang in languages:
            if lang not in cable["data"]:
                continue
            schema = build_schema(cable, lang)
            filename = f"{cable['common']['slug']}.json"
            filepath = os.path.join(BASE_DIR, lang, filename)
            os.makedirs(os.path.join(BASE_DIR, lang), exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(schema, f, indent=2, ensure_ascii=False)
                f.write("\n")
            print(f"  ✓ {lang}/{filename}")
            count += 1
    print(f"\nTotal: {count} fitxers generats")


if __name__ == "__main__":
    main()
