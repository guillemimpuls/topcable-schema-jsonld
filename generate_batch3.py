#!/usr/bin/env python3
"""
Generate JSON-LD schemas for Top Cable Batch 3 (10 cables × multiple languages)
Following v5.1 specification with rules 13-16
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# SHARED STRUCTURES
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
AUDIENCE_SOLAR = {
    "en": "Electrical Distributors, Electrical Installers, Engineers (Solar & Photovoltaic Projects)",
    "fr": "Distributeurs électriques, Installateurs électriques, Ingénieurs (Projets solaires et photovoltaïques)",
    "es": "Distribuidores eléctricos, Instaladores eléctricos, Ingenieros (Proyectos solares y fotovoltaicos)",
}
AUDIENCE_MARINE = {
    "en": "Electrical Distributors, Electrical Installers, Engineers (Marine & Shipbuilding Projects)",
    "fr": "Distributeurs électriques, Installateurs électriques, Ingénieurs (Projets maritimes et construction navale)",
    "es": "Distribuidores eléctricos, Instaladores eléctricos, Ingenieros (Proyectos marítimos y construcción naval)",
}

MATERIAL_COPPER_FLEX = {
    "en": "Copper, class 5 (flexible)",
    "fr": "Cuivre, classe 5 (souple)",
    "es": "Cobre, clase 5 (flexible)",
}
MATERIAL_TINNED_COPPER_FLEX = {
    "en": "Tinned copper, class 5 (flexible)",
    "fr": "Cuivre étamé, classe 5 (souple)",
    "es": "Cobre estañado, clase 5 (flexible)",
}

BREADCRUMB_FAMILIES = {
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
    "solar": {
        "en": {"name": "Solar Cables", "url": "https://www.topcable.com/solar-cables/"},
        "fr": {"name": "Câbles solaires", "url": "https://www.topcable.com/fr/cables-solaires/"},
        "es": {"name": "Cables solares", "url": "https://www.topcable.com/es/cables-solares/"},
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
        "screen": "Screen",
        "layup": "Lay-up",
        "rated_voltage": "Rated Voltage",
        "max_temp": "Maximum Conductor Temperature",
        "max_sc_temp": "Maximum Short-Circuit Temperature",
        "min_service_temp": "Minimum Service Temperature",
        "min_install_temp": "Minimum Installation Temperature",
        "flame_nonprop": "Flame Non-Propagation",
        "fire_nonprop": "Fire Non-Propagation",
        "fire_resistant": "Fire Resistant",
        "cpr": "CPR Classification",
        "halogen_free": "Halogen Free",
        "low_corrosive_gases": "Low Corrosive Gases Emission",
        "low_smoke": "Low Smoke Emission",
        "light_transmittance": "Light Transmittance",
        "reduced_halogens": "Reduced Halogens",
        "min_bending": "Minimum Bending Radius",
        "impact": "Impact Resistance",
        "chemical_oil": "Chemical & Oil Resistance",
        "uv": "UV Resistance",
        "ozone": "Ozone Resistance",
        "water": "Water Resistance",
        "installation": "Installation Conditions",
        "standards_ref": "Standards (According To)",
        "standards_approvals": "Standards and Approvals",
        "applications": "Typical Applications",
    },
    "fr": {
        "conductor": "Conducteur",
        "insulation": "Isolation",
        "outer_sheath": "Gaine extérieure",
        "inner_covering": "Gaine intérieure",
        "screen": "Écran",
        "layup": "Assemblage",
        "rated_voltage": "Tension nominale",
        "max_temp": "Température maximale du conducteur",
        "max_sc_temp": "Température maximale de court-circuit",
        "min_service_temp": "Température minimale de service",
        "min_install_temp": "Température minimale d'installation",
        "flame_nonprop": "Non-propagation de la flamme",
        "fire_nonprop": "Non-propagation de l'incendie",
        "fire_resistant": "Résistance au feu",
        "cpr": "Classification CPR",
        "halogen_free": "Sans halogène",
        "low_corrosive_gases": "Faible émission de gaz corrosifs",
        "low_smoke": "Faible émission de fumée",
        "light_transmittance": "Transmittance lumineuse",
        "reduced_halogens": "Halogènes réduits",
        "min_bending": "Rayon de courbure minimum",
        "impact": "Résistance aux chocs",
        "chemical_oil": "Résistance chimique et aux huiles",
        "uv": "Résistance aux UV",
        "ozone": "Résistance à l'ozone",
        "water": "Résistance à l'eau",
        "installation": "Conditions d'installation",
        "standards_ref": "Normes (Selon)",
        "standards_approvals": "Normes et approbations",
        "applications": "Applications typiques",
    },
    "es": {
        "conductor": "Conductor",
        "insulation": "Aislamiento",
        "outer_sheath": "Cubierta exterior",
        "inner_covering": "Cubierta interior",
        "screen": "Pantalla",
        "layup": "Cableado",
        "rated_voltage": "Tensión nominal",
        "max_temp": "Temperatura máxima del conductor",
        "max_sc_temp": "Temperatura máxima de cortocircuito",
        "min_service_temp": "Temperatura mínima de servicio",
        "min_install_temp": "Temperatura mínima de instalación",
        "flame_nonprop": "No propagación de la llama",
        "fire_nonprop": "No propagación del incendio",
        "fire_resistant": "Resistencia al fuego",
        "cpr": "Clasificación CPR",
        "halogen_free": "Libre de halógenos",
        "low_corrosive_gases": "Baja emisión de gases corrosivos",
        "low_smoke": "Baja emisión de humo",
        "light_transmittance": "Transmitancia luminosa",
        "reduced_halogens": "Halógenos reducidos",
        "min_bending": "Radio mínimo de curvatura",
        "impact": "Resistencia al impacto",
        "chemical_oil": "Resistencia química y a aceites",
        "uv": "Resistencia a los UV",
        "ozone": "Resistencia al ozono",
        "water": "Resistencia al agua",
        "installation": "Condiciones de instalación",
        "standards_ref": "Normas (Según)",
        "standards_approvals": "Normas y aprobaciones",
        "applications": "Aplicaciones típicas",
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
        slug = c.get(f"slug_{lang}", c["slug"])
        page_url = f"https://www.topcable.com/{lang}/cable/{slug}/"
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
CONDUCTOR_TINNED_COPPER_FLEX = {
    "en": "Tinned copper, class 5 (flexible) according to EN 60228 and IEC 60228",
    "fr": "Cuivre étamé, classe 5 (souple) selon EN 60228 et IEC 60228",
    "es": "Cobre estañado, clase 5 (flexible) según UNE-EN 60228 e IEC 60228",
}

SC_TEMP_250 = {"en": "250 (max. 5 s)", "fr": "250 (max. 5 s)", "es": "250 (máximo 5 s)"}
SC_TEMP_160 = {"en": "160 (max. 5 s)", "fr": "160 (max. 5 s)", "es": "160 (máximo 5 s)"}

MIN_TEMP_FIXED = {
    "en": "-40 (fixed and protected installations)",
    "fr": "-40 (installations fixes et protégées)",
    "es": "-40 (estático con protección)",
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
FIRE_NONPROP_3_22 = {
    "en": "Fire non-propagation according to EN 60332-3-22 / IEC 60332-3-22",
    "fr": "Non-propagation de l'incendie selon EN 60332-3-22 et IEC 60332-3-22",
    "es": "No propagación del incendio según UNE-EN 60332-3-22 / IEC 60332-3-22",
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

REDUCED_HALOGENS = {
    "en": "Reduced halogens, Chlorine < 15%",
    "fr": "Halogènes réduits, Chlore < 15%",
    "es": "Halógenos reducidos, Cloro < 15%",
}

IMPACT_AG2 = {"en": "AG2 Medium severity", "fr": "AG2 Sévérité moyenne", "es": "AG2 Medio"}

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

WATER_AD5 = {"en": "AD5 Jets", "fr": "AD5 Jets", "es": "AD5 Chorros"}

INSTALL_FULL = {
    "en": "Open Air. Buried. In conduit.",
    "fr": "À l'air libre. Enterré. En canalisation.",
    "es": "Al aire. Enterrado. Entubado.",
}
INSTALL_CONDUIT = {
    "en": "In conduit",
    "fr": "En canalisation",
    "es": "Entubado",
}
INSTALL_OPEN = {"en": "Open Air", "fr": "À l'air libre", "es": "Al aire"}

IMG_BASE = "https://www.topcable.com/wp-content/uploads/2025/07/"
IMG_BASE_12 = "https://www.topcable.com/wp-content/uploads/2025/12/"


# ============================================================
# CABLE 1: TOXFREE® PLUS 331 LSZH RZ1-K (AS+) FR2
# ============================================================
def cable_plus331(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "Mica tape + Cross-linked polyethylene type XLPE according to IEC 60502-1",
            "fr": "Ruban de mica + Polyéthylène réticulé type XLPE selon IEC 60502-1",
            "es": "Cinta de mica + Polietileno reticulado tipo XLPE según IEC 60502-1",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "Low smoke halogen free and fire resistant polyolefin. Orange colour",
            "fr": "Polyoléfine sans halogène à faible émission de fumée et résistante au feu. Couleur orange",
            "es": "Poliolefina libre de halógenos, baja emisión de humo y resistente al fuego. Color naranja",
        }[lang]),
        make_prop(lang, "rated_voltage", "0.6/1", "kV"),
        make_prop(lang, "max_temp", "90", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_250[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED[lang], "°C"),
        make_prop(lang, "min_install_temp", "0", "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "fire_nonprop", FIRE_NONPROP[lang]),
        make_prop(lang, "fire_resistant", {
            "en": "Fire resistant (PH120) minimum 120 minutes at 840°C according to IEC 60331-2 / EN 50200 (cable diameter ≤ 20 mm) and IEC 60331-1 / EN 50362 (cable diameter > 20 mm). BS 6387 Category C (180 minutes at 950°C) W & Z",
            "fr": "Résistance au feu (PH120) minimum 120 minutes à 840°C selon IEC 60331-2 / EN 50200 (diamètre câble ≤ 20 mm) et IEC 60331-1 / EN 50362 (diamètre câble > 20 mm). BS 6387 Catégorie C (180 minutes à 950°C) W et Z",
            "es": "Resistencia al fuego (PH120) mínimo 120 minutos a 840°C según IEC 60331-2 / EN 50200 (diámetro cable ≤ 20 mm) e IEC 60331-1 / EN 50362 (diámetro cable > 20 mm). BS 6387 Categoría C (180 minutos a 950°C) W y Z",
        }[lang]),
        make_prop(lang, "cpr", {
            "en": "B2ca-s1a, d1, a1 or Cca-s1b, d1, a1 (according to cross-section) according to EN 50575",
            "fr": "B2ca-s1a, d1, a1 ou Cca-s1b, d1, a1 (selon la section) selon EN 50575",
            "es": "B2ca-s1a, d1, a1 o Cca-s1b, d1, a1 (según la sección) según EN 50575",
        }[lang]),
        make_prop(lang, "halogen_free", HALOGEN_FREE[lang]),
        make_prop(lang, "low_corrosive_gases", LOW_CORROSIVE_GASES[lang]),
        make_prop(lang, "low_smoke", LOW_SMOKE_61034[lang]),
        make_prop(lang, "light_transmittance", "> 60%"),
        make_prop(lang, "min_bending", {
            "en": "5x cable diameter",
            "fr": "5x diamètre du câble",
            "es": "5x diámetro del cable",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_ACCEPTABLE[lang]),
        make_prop(lang, "uv", UV_EN50618[lang]),
        make_prop(lang, "water", WATER_AD5[lang]),
        make_prop(lang, "installation", INSTALL_FULL[lang]),
        make_prop(lang, "standards_ref", "IEC 60502-1, UNE 211025"),
        make_prop(lang, "standards_approvals", "AENOR, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Emergency circuits, Fire alarm systems, Tunnels",
            "fr": "Circuits de secours, Systèmes d'alarme incendie, Tunnels",
            "es": "Circuitos de emergencia, Sistemas de alarma contra incendios, Túneles",
        }[lang]),
    ]

CABLE_1 = {
    "common": {
        "slug": "toxfree-plus-331-zh-rz1-k-as",
        "slug_fr": "toxfreeplus-331-lszh-rz1-k-as-fr2",
        "slug_es": "toxfreeplus-331-lszh-rz1-k-as-fr2",
        "mpn": "RZ1-K (AS+) FR2",
        "brand": "TOXFREE®",
        "family": "lszh",
        "datasheet_slug": "toxfree-plus-331-lszh-rz1-k-asplus-fr2",
        "images": [
            IMG_BASE + "topcable-rz1-k-as-fr2-fire-resistant-lszh-power-cable-for-emergency-circuits-01.png",
            IMG_BASE + "TOPCABLE_TOXFREE_PLUS_331_RZ1_K_AS_FR2.webp",
            IMG_BASE + "bobina_naranja.png"
        ],
    },
    "data": {
        "en": {
            "name": "TOXFREE® PLUS 331 LSZH RZ1-K (AS+) FR2",
            "description": "Fire resistant LSZH power cable for emergency circuits. ACCORDING TO: IEC 60502-1 / UNE 211025. TOXFREE® PLUS 331 LSZH RZ1-K (AS+) FR2 is a fire resistant cable, specially designed to ensure the power supply to emergency circuits in the event of fire. Maintained circuit integrity during fire (PH120). Highly recommended for emergency lighting, fire alarms, evacuation systems, ventilation, and communication circuits in tunnels and high-occupancy buildings.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_LSZH["en"],
            "properties": cable_plus331("en"),
        },
        "fr": {
            "name": "TOXFREE® PLUS 331 LSZH RZ1-K (AS+) FR2",
            "description": "Câble d'alimentation LSZH résistant au feu pour les circuits de secours. SELON : IEC 60502-1 / UNE 211025. Le TOXFREE® PLUS 331 LSZH RZ1-K (AS+) FR2 est un câble résistant au feu, spécialement conçu pour assurer l'alimentation des circuits de secours en cas d'incendie. Intégrité du circuit maintenue pendant l'incendie (PH120). Fortement recommandé pour l'éclairage de secours, les alarmes incendie, les systèmes d'évacuation, la ventilation et les circuits de communication dans les tunnels et les bâtiments à forte occupation.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_LSZH["fr"],
            "properties": cable_plus331("fr"),
        },
        "es": {
            "name": "TOXFREE® PLUS 331 LSZH RZ1-K (AS+) FR2",
            "description": "Cable de potencia LSZH resistente al fuego para circuitos de emergencia. NORMAS DE REFERENCIA: IEC 60502-1 / UNE 211025. El TOXFREE® PLUS 331 LSZH RZ1-K (AS+) FR2 es un cable resistente al fuego, especialmente diseñado para garantizar la alimentación eléctrica de los circuitos de emergencia en caso de incendio. Integridad del circuito mantenida durante el incendio (PH120). Altamente recomendado para iluminación de emergencia, alarmas contra incendios, sistemas de evacuación, ventilación y circuitos de comunicación en túneles y edificios de alta ocupación.",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_LSZH["es"],
            "properties": cable_plus331("es"),
        },
    },
}


# ============================================================
# CABLE 2: TOXFREE® LSZH ES05Z1-K & H07Z1-K
# ============================================================
def cable_es05z1k(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "LSZH polyolefin according to EN 50525-3-31",
            "fr": "Polyoléfine LSZH selon EN 50525-3-31",
            "es": "Poliolefina LSZH según EN 50525-3-31",
        }[lang]),
        make_prop(lang, "rated_voltage", {
            "en": "300/500 V (ES05Z1-K up to 1 mm²) and 450/750 V (H07Z1-K from 1.5 mm²)",
            "fr": "300/500 V (ES05Z1-K jusqu'à 1 mm²) et 450/750 V (H07Z1-K à partir de 1,5 mm²)",
            "es": "300/500 V (ES05Z1-K hasta 1 mm²) y 450/750 V (H07Z1-K desde 1,5 mm²)",
        }[lang]),
        make_prop(lang, "max_temp", "70", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_160[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED[lang], "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "fire_nonprop", FIRE_NONPROP[lang]),
        make_prop(lang, "cpr", {
            "en": "B2ca-s1a, d1, a1 according to EN 50575",
            "fr": "B2ca-s1a, d1, a1 selon EN 50575",
            "es": "B2ca-s1a, d1, a1 según EN 50575",
        }[lang]),
        make_prop(lang, "halogen_free", HALOGEN_FREE[lang]),
        make_prop(lang, "low_corrosive_gases", LOW_CORROSIVE_GASES[lang]),
        make_prop(lang, "low_smoke", LOW_SMOKE_61034[lang]),
        make_prop(lang, "light_transmittance", "> 80%"),
        make_prop(lang, "min_bending", {
            "en": "5x cable diameter",
            "fr": "5x diamètre du câble",
            "es": "5x diámetro exterior",
        }[lang]),
        make_prop(lang, "chemical_oil", CHEM_ACCEPTABLE[lang]),
        make_prop(lang, "installation", INSTALL_CONDUIT[lang]),
        make_prop(lang, "standards_ref", "EN 50525-3-31, UNE 211002"),
        make_prop(lang, "standards_approvals", "SEC, HAR, BUREAU VERITAS, AENOR, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Domestic use, Public places, Electrical panel wiring",
            "fr": "Usage domestique, Lieux publics, Câblage de tableaux électriques",
            "es": "Uso doméstico, Lugares públicos, Cableado de cuadros eléctricos",
        }[lang]),
    ]

CABLE_2 = {
    "common": {
        "slug": "toxfree-lszh-es05z1-k-h07z1-k",
        "mpn": "ES05Z1-K & H07Z1-K",
        "brand": "TOXFREE®",
        "family": "lszh",
        "datasheet_slug": "toxfree-lszh-es05z1-k-h07z1-k",
        "images": [
            IMG_BASE + "topcable-es05z1-k-h07z1-k-flexible-and-halogen-free-power-cable-for-electrical-panel-wiring-01.png",
            IMG_BASE + "TOPCABLE_TOXFREE_ZH_ES05Z1_K_H07Z1_K.webp",
            IMG_BASE + "bobina_verde.png"
        ],
    },
    "data": {
        "en": {
            "name": "TOXFREE® LSZH ES05Z1-K & H07Z1-K",
            "description": "Flexible and halogen free power cable for electrical panel wiring. ACCORDING TO: EN 50525-3-31 / UNE 211002. TOXFREE® LSZH ES05Z1-K & H07Z1-K is a LSZH safety cable highly recommended for use in public places. In the event of fire, it does not emit toxic gases, nor does it give off corrosive gases, avoiding any possible damage to people or electronic equipment. Highly recommended for use in public places such as: hospitals, schools, museums, airports, bus terminals, shopping centres, offices, and laboratories.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_LSZH["en"],
            "properties": cable_es05z1k("en"),
        },
        "fr": {
            "name": "TOXFREE® LSZH ES05Z1-K & H07Z1-K",
            "description": "Câble d'alimentation souple et sans halogène pour le câblage de tableaux électriques. SELON : EN 50525-3-31 / UNE 211002. Le TOXFREE® LSZH ES05Z1-K & H07Z1-K est un câble de sécurité LSZH fortement recommandé pour une utilisation dans les lieux publics. En cas d'incendie, il n'émet pas de gaz toxiques ni de gaz corrosifs, évitant tout dommage aux personnes ou aux équipements électroniques. Fortement recommandé pour les lieux publics tels que : hôpitaux, écoles, musées, aéroports, gares routières, centres commerciaux, bureaux et laboratoires.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_LSZH["fr"],
            "properties": cable_es05z1k("fr"),
        },
        "es": {
            "name": "TOXFREE® LSZH ES05Z1-K & H07Z1-K",
            "description": "Cable flexible libre de halógenos para cableado de cuadros eléctricos. NORMAS DE REFERENCIA: EN 50525-3-31 / UNE 211002. El TOXFREE® LSZH ES05Z1-K & H07Z1-K es un cable de seguridad LSZH altamente recomendado para uso en lugares públicos. En caso de incendio, no emite gases tóxicos ni gases corrosivos, evitando cualquier daño a personas o equipos electrónicos. Muy recomendable para lugares públicos como: hospitales, escuelas, museos, aeropuertos, terminales de autobuses, centros comerciales, oficinas y laboratorios.",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_LSZH["es"],
            "properties": cable_es05z1k("es"),
        },
    },
}


# ============================================================
# CABLE 3: TOXFREE® LSZH OUTDOOR H07Z1-K type 2 CuSn
# ============================================================
def cable_outdoor_h07z1k(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_TINNED_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "LSZH polyolefin, UV resistant according to EN 50525-3-31",
            "fr": "Polyoléfine LSZH, résistante aux UV selon EN 50525-3-31",
            "es": "Poliolefina LSZH, resistente a los UV según EN 50525-3-31",
        }[lang]),
        make_prop(lang, "rated_voltage", "450/750", "V"),
        make_prop(lang, "max_temp", "70", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_160[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED[lang], "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "fire_nonprop", FIRE_NONPROP_3_24[lang]),
        make_prop(lang, "cpr", {
            "en": "B2ca-s1a, d1, a1 according to EN 50575",
            "fr": "B2ca-s1a, d1, a1 selon EN 50575",
            "es": "B2ca-s1a, d1, a1 según EN 50575",
        }[lang]),
        make_prop(lang, "halogen_free", HALOGEN_FREE[lang]),
        make_prop(lang, "low_corrosive_gases", LOW_CORROSIVE_GASES[lang]),
        make_prop(lang, "low_smoke", LOW_SMOKE_61034[lang]),
        make_prop(lang, "light_transmittance", "> 80%"),
        make_prop(lang, "min_bending", {
            "en": "5x cable diameter",
            "fr": "5x diamètre du câble",
            "es": "5x diámetro exterior",
        }[lang]),
        make_prop(lang, "chemical_oil", CHEM_EXCELLENT[lang]),
        make_prop(lang, "uv", UV_EN50618[lang]),
        make_prop(lang, "ozone", {
            "en": "Ozone resistant according to EN 50618",
            "fr": "Résistance à l'ozone selon EN 50618",
            "es": "Resistencia al ozono según EN 50618",
        }[lang]),
        make_prop(lang, "installation", INSTALL_OPEN[lang]),
        make_prop(lang, "standards_ref", "EN 50525-3-31, UNE 211002"),
        make_prop(lang, "standards_approvals", "HAR, BUREAU VERITAS, AENOR, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Solar installations, Photovoltaic grounding, Outdoor installations",
            "fr": "Installations solaires, Mise à la terre photovoltaïque, Installations extérieures",
            "es": "Instalaciones solares, Puesta a tierra fotovoltaica, Instalaciones exteriores",
        }[lang]),
    ]

CABLE_3 = {
    "common": {
        "slug": "toxfree-lszh-outdoor-h07z1-k-type-2-cusn",
        "mpn": "OUTDOOR H07Z1-K CuSn",
        "brand": "TOXFREE®",
        "family": "solar",
        "datasheet_slug": "toxfree-lszh-outdoor-h07z1-k-type-2-cusn",
        "images": [
            IMG_BASE + "topcable-h07z1-k-type-2-cusn-grounding-cable-with-tinned-copper-conductor-01.webp",
            IMG_BASE + "TOPCABLE_TOXFREE_ZH_OUTDOOR_H07Z1_K.webp",
            IMG_BASE + "bobina_verde.png"
        ],
    },
    "data": {
        "en": {
            "name": "TOXFREE® LSZH OUTDOOR H07Z1-K type 2 CuSn",
            "description": "Grounding cable with tinned copper conductor. ACCORDING TO: EN 50525-3-31 / UNE 211002. TOXFREE® LSZH OUTDOOR H07Z1-K type 2 CuSn is a cable specially designed for grounding in outdoor installations. The tinned copper conductor and special insulation compounds make it highly resistant to corrosion and UV degradation, preventing galvanic corrosion when connecting dissimilar metals. LSZH halogen-free cable with the highest CPR classification (B2ca-s1a, d1, a1) and UV protection according to solar standard EN 50618.",
            "material": MATERIAL_TINNED_COPPER_FLEX["en"],
            "audience": AUDIENCE_SOLAR["en"],
            "properties": cable_outdoor_h07z1k("en"),
        },
        "fr": {
            "name": "TOXFREE® LSZH OUTDOOR H07Z1-K type 2 CuSn",
            "description": "Câble de mise à la terre avec conducteur en cuivre étamé. SELON : EN 50525-3-31 / UNE 211002. Le TOXFREE® LSZH OUTDOOR H07Z1-K type 2 CuSn est un câble spécialement conçu pour les mises à la terre dans les installations extérieures. Le conducteur en cuivre étamé et les composés spéciaux de son isolation le rendent hautement résistant à la corrosion et à la dégradation UV, évitant la corrosion galvanique lors de la connexion de métaux de potentiel différent. Câble LSZH sans halogène avec la classification CPR la plus élevée (B2ca-s1a, d1, a1) et protection UV selon la norme solaire EN 50618.",
            "material": MATERIAL_TINNED_COPPER_FLEX["fr"],
            "audience": AUDIENCE_SOLAR["fr"],
            "properties": cable_outdoor_h07z1k("fr"),
        },
        "es": {
            "name": "TOXFREE® LSZH OUTDOOR H07Z1-K type 2 CuSn",
            "description": "Cable para toma a tierra con conductor de cobre estañado. NORMAS DE REFERENCIA: EN 50525-3-31 / UNE 211002. El TOXFREE® LSZH OUTDOOR H07Z1-K type 2 CuSn es un cable especialmente diseñado para las conexiones de tierra en instalaciones exteriores. El conductor de cobre estañado y los compuestos especiales de su cubierta lo hacen altamente resistente a la corrosión y a la degradación por rayos UV, evitando el par galvánico al conectar metales de diferente potencial. Cable LSZH libre de halógenos con la máxima clasificación CPR (B2ca-s1a, d1, a1) y protección UV según la norma solar EN 50618.",
            "material": MATERIAL_TINNED_COPPER_FLEX["es"],
            "audience": AUDIENCE_SOLAR["es"],
            "properties": cable_outdoor_h07z1k("es"),
        },
    },
}


# ============================================================
# CABLE 4: TOPFLEX® V-K H05V-K & H07V-K
# ============================================================
def cable_topflex_vk(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "PVC (flexible) extra-sliding according to EN 50525-2-31",
            "fr": "PVC (souple) extra-glissant selon EN 50525-2-31",
            "es": "PVC (flexible) extra-deslizante según EN 50525-2-31",
        }[lang]),
        make_prop(lang, "rated_voltage", {
            "en": "300/500 V (H05V-K up to 1 mm²) and 450/750 V (H07V-K from 1.5 mm²)",
            "fr": "300/500 V (H05V-K jusqu'à 1 mm²) et 450/750 V (H07V-K à partir de 1,5 mm²)",
            "es": "300/500 V (H05V-K hasta 1 mm²) y 450/750 V (H07V-K desde 1,5 mm²)",
        }[lang]),
        make_prop(lang, "max_temp", "70", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_160[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED[lang], "°C"),
        make_prop(lang, "min_install_temp", "5", "°C"),
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
            "es": "5x diámetro exterior",
        }[lang]),
        make_prop(lang, "chemical_oil", CHEM_ACCEPTABLE[lang]),
        make_prop(lang, "installation", INSTALL_CONDUIT[lang]),
        make_prop(lang, "standards_ref", "EN 50525-2-31, IEC 60227-3"),
        make_prop(lang, "standards_approvals", "SEC, HAR, AENOR, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Cabinet wiring, Domestic use, Industrial facilities",
            "fr": "Câblage d'armoires, Usage domestique, Installations industrielles",
            "es": "Cableado de cuadros eléctricos, Uso doméstico, Instalaciones industriales",
        }[lang]),
    ]

CABLE_4 = {
    "common": {
        "slug": "topflex-v-k-h05v-k-and-h07v-k",
        "slug_fr": "topflex-v-k-h05v-k-et-h07v-k",
        "slug_es": "topflex-v-k-h05v-k-y-h07v-k",
        "mpn": "H05V-K & H07V-K",
        "brand": "TOPFLEX®",
        "family": "pvc",
        "datasheet_slug": "topflex-v-k-h05v-k-h07v-k",
        "images": [
            IMG_BASE + "topcable-h05v-k-h07v-k-cable-for-electric-cabinet-wiring-and-domestic-use-01.webp",
            IMG_BASE + "TOPCABLE_TOPFLEX_VK_H05VK_H07VK.webp",
            IMG_BASE + "bobina_gris.png"
        ],
    },
    "data": {
        "en": {
            "name": "TOPFLEX® V-K H05V-K & H07V-K",
            "description": "Cable for electric cabinet wiring and domestic use. ACCORDING TO: EN 50525-2-31 / IEC 60227-3. TOPFLEX® V-K H05V-K & H07V-K is a flexible cable recommended for complex layouts. Specially designed for installations requiring flexibility due to layout complexity, domestic wiring, equipment wiring, distributors, cabinets, lighting, and installation under false ceilings.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_DOMESTIC["en"],
            "properties": cable_topflex_vk("en"),
        },
        "fr": {
            "name": "TOPFLEX® V-K H05V-K & H07V-K",
            "description": "Câble pour le câblage d'armoires électriques et usage domestique. SELON : EN 50525-2-31 / IEC 60227-3. Le TOPFLEX® V-K H05V-K & H07V-K est un câble souple recommandé pour les tracés complexes. Spécialement conçu pour les installations nécessitant de la flexibilité, le câblage domestique, le câblage d'équipements, les distributeurs, armoires, éclairage et installation sous faux plafonds.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_DOMESTIC["fr"],
            "properties": cable_topflex_vk("fr"),
        },
        "es": {
            "name": "TOPFLEX® V-K H05V-K & H07V-K",
            "description": "Cable para cableado de cuadros eléctricos y uso doméstico. NORMAS DE REFERENCIA: EN 50525-2-31 / IEC 60227-3. El TOPFLEX® V-K H05V-K & H07V-K es un cable flexible recomendado para trazados complejos. Especialmente diseñado para instalaciones que requieren flexibilidad, cableado doméstico, cableado de equipos, distribuidores, armarios, iluminación e instalación bajo falsos techos.",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_DOMESTIC["es"],
            "properties": cable_topflex_vk("es"),
        },
    },
}


# ============================================================
# CABLE 5: FLEXTEL® 140 H05VV5-F
# ============================================================
def cable_flextel140(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "PVC (flexible) according to EN 50525-2-51",
            "fr": "PVC (souple) selon EN 50525-2-51",
            "es": "PVC (flexible) según EN 50525-2-51",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "PVC (flexible) and oil resistant. Grey colour",
            "fr": "PVC (souple) et résistant aux huiles. Couleur grise",
            "es": "PVC (flexible) y resistente a aceites. Color gris",
        }[lang]),
        make_prop(lang, "rated_voltage", "300/500", "V"),
        make_prop(lang, "max_temp", "70", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_160[lang], "°C"),
        make_prop(lang, "min_service_temp", {
            "en": "5 (mobile use)",
            "fr": "5 (service mobile)",
            "es": "5 (servicio móvil)",
        }[lang], "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "cpr", {
            "en": "Eca according to EN 50575",
            "fr": "Eca selon EN 50575",
            "es": "Eca según EN 50575",
        }[lang]),
        make_prop(lang, "min_bending", {
            "en": "3x cable diameter (< 12 mm), 4x cable diameter (≥ 12 mm)",
            "fr": "3x diamètre du câble (< 12 mm), 4x diamètre du câble (≥ 12 mm)",
            "es": "3x diámetro del cable (< 12 mm), 4x diámetro del cable (≥ 12 mm)",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_EXCELLENT[lang]),
        make_prop(lang, "water", WATER_AD5[lang]),
        make_prop(lang, "installation", {
            "en": "Open Air. In conduit.",
            "fr": "À l'air libre. En canalisation.",
            "es": "Al aire. Entubado.",
        }[lang]),
        make_prop(lang, "standards_ref", "EN 50525-2-51, IEC 60227"),
        make_prop(lang, "standards_approvals", "HAR, AENOR, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Signalling and control systems, Robotics, Light mobile services",
            "fr": "Systèmes de signalisation et de contrôle, Robotique, Services mobiles légers",
            "es": "Sistemas de señalización y control, Robótica, Servicios móviles ligeros",
        }[lang]),
    ]

CABLE_5 = {
    "common": {
        "slug": "flextel-140-h05vv5-f",
        "mpn": "H05VV5-F",
        "brand": "FLEXTEL®",
        "family": "pvc",
        "datasheet_slug": "flextel-140-h05vv5-f",
        "images": [
            IMG_BASE + "topcable-h05vv5-f-140-flexible-oil-resistant-control-cable-for-mobile-use-01.png",
            IMG_BASE + "TOPCABLE_FLEXTEL_140_H05VV5_F.webp",
            IMG_BASE + "bobina_gris.png"
        ],
    },
    "data": {
        "en": {
            "name": "FLEXTEL® 140 H05VV5-F",
            "description": "Flexible oil resistant control cable, for mobile use. ACCORDING TO: EN 50525-2-51 / IEC 60227. FLEXTEL® 140 H05VV5-F is a flexible control cable designed for signalling and control systems and robotics and light mobile uses. The special vinylic outer sheath compound is particularly resistant to mineral oils and other chemical agents.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_INDUSTRIAL["en"],
            "properties": cable_flextel140("en"),
        },
        "fr": {
            "name": "FLEXTEL® 140 H05VV5-F",
            "description": "Câble de contrôle souple résistant aux huiles, pour utilisation mobile. SELON : EN 50525-2-51 / IEC 60227. Le FLEXTEL® 140 H05VV5-F est un câble de contrôle souple conçu pour les systèmes de signalisation et de contrôle, la robotique et les utilisations mobiles légères. Le composé spécial de la gaine extérieure vinylique est particulièrement résistant aux huiles minérales et autres agents chimiques.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_INDUSTRIAL["fr"],
            "properties": cable_flextel140("fr"),
        },
        "es": {
            "name": "FLEXTEL® 140 H05VV5-F",
            "description": "Cable flexible de control resistente a los aceites, para servicio móvil. NORMAS DE REFERENCIA: EN 50525-2-51 / IEC 60227. El FLEXTEL® 140 H05VV5-F es un cable de control flexible diseñado para sistemas de señalización y control, robótica y servicios móviles ligeros. El compuesto especial de la cubierta exterior vinílica es particularmente resistente a los aceites minerales y otros agentes químicos.",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_INDUSTRIAL["es"],
            "properties": cable_flextel140("es"),
        },
    },
}


# ============================================================
# CABLE 6: FLEXTEL® 200 VV-K
# ============================================================
def cable_flextel200(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "PVC (flexible) according to IEC 60502-1",
            "fr": "PVC (souple) selon IEC 60502-1",
            "es": "PVC (flexible) según IEC 60502-1",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "PVC (flexible). Black colour",
            "fr": "PVC (souple). Couleur noire",
            "es": "PVC (flexible). Color negro",
        }[lang]),
        make_prop(lang, "rated_voltage", "0.6/1", "kV"),
        make_prop(lang, "max_temp", "70", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_160[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED[lang], "°C"),
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
            "es": "5x diámetro exterior",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_GOOD[lang]),
        make_prop(lang, "uv", {
            "en": "UV Resistant according to UNE 211605 annex A.2",
            "fr": "Résistance aux UV selon UNE 211605 annexe A.2",
            "es": "Resistencia a los rayos ultravioleta según UNE 211605 anexo A.2",
        }[lang]),
        make_prop(lang, "water", WATER_AD5[lang]),
        make_prop(lang, "installation", INSTALL_FULL[lang]),
        make_prop(lang, "standards_ref", "IEC 60502-1"),
        make_prop(lang, "standards_approvals", "RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Industrial facilities, Connection of machinery, Motor connections",
            "fr": "Installations industrielles, Connexion de machines, Connexion de moteurs",
            "es": "Instalaciones industriales, Conexión de maquinaria, Conexión de motores",
        }[lang]),
    ]

CABLE_6 = {
    "common": {
        "slug": "flextel-200-vv-k",
        "mpn": "VV-K",
        "brand": "FLEXTEL®",
        "family": "pvc",
        "datasheet_slug": "flextel-200-vv-k",
        "images": [
            IMG_BASE + "topcable-vv-k-flexible-0-6-1kv-control-cable-01.png",
            IMG_BASE + "TOPCABLE_FLEXTEL_200_VV_K.webp",
            IMG_BASE + "bobina_negra.png"
        ],
    },
    "data": {
        "en": {
            "name": "FLEXTEL® 200 VV-K",
            "description": "Flexible 0,6/1 kV control cable. ACCORDING TO: IEC 60502-1. FLEXTEL® 200 VV-K is ideal for connecting motors or frequency converters. Suitable for fixed installations with complex layouts where flexible cables are required, and for industrial environments requiring resistance to oils, chemicals, and mechanical stress.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_INDUSTRIAL["en"],
            "properties": cable_flextel200("en"),
        },
        "fr": {
            "name": "FLEXTEL® 200 VV-K",
            "description": "Câble de contrôle souple 0,6/1 kV. SELON : IEC 60502-1. Le FLEXTEL® 200 VV-K est idéal pour connecter des moteurs ou des variateurs de fréquence. Adapté aux installations fixes avec des tracés complexes nécessitant des câbles souples, et pour les environnements industriels nécessitant une résistance aux huiles, produits chimiques et contraintes mécaniques.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_INDUSTRIAL["fr"],
            "properties": cable_flextel200("fr"),
        },
        "es": {
            "name": "FLEXTEL® 200 VV-K",
            "description": "Cable flexible de control 0,6/1 kV. NORMAS DE REFERENCIA: IEC 60502-1. El FLEXTEL® 200 VV-K es ideal para conectar motores o convertidores de frecuencia. Adecuado para instalaciones fijas con trazados complejos que requieren cables flexibles, y para entornos industriales que requieren resistencia a aceites, productos químicos y estrés mecánico.",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_INDUSTRIAL["es"],
            "properties": cable_flextel200("es"),
        },
    },
}


# ============================================================
# CABLE 7: SCREENFLEX® 110/200 LiYCY VC4V-K
# ============================================================
def cable_screenflex(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "PVC (flexible) according to EN 50525",
            "fr": "PVC (souple) selon EN 50525",
            "es": "PVC (flexible) según EN 50525",
        }[lang]),
        make_prop(lang, "screen", {
            "en": "Overlapping aluminium-polyester tape screen with 100% coverage and tinned copper drain wire",
            "fr": "Écran en bande aluminium-polyester à recouvrement avec couverture 100% et drain en cuivre étamé",
            "es": "Pantalla de cinta aluminio-poliéster solapada con cobertura 100% y drenaje de cobre estañado",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "PVC (flexible). Black or grey colour",
            "fr": "PVC (souple). Couleur noire ou grise",
            "es": "PVC (flexible). Color negro o gris",
        }[lang]),
        make_prop(lang, "rated_voltage", {
            "en": "300/500 V (up to 1.5 mm²) and 0.6/1 kV (from 2.5 mm²)",
            "fr": "300/500 V (jusqu'à 1,5 mm²) et 0,6/1 kV (à partir de 2,5 mm²)",
            "es": "300/500 V (hasta 1,5 mm²) y 0,6/1 kV (desde 2,5 mm²)",
        }[lang]),
        make_prop(lang, "max_temp", "70", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_160[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED[lang], "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "fire_nonprop", {
            "en": "Fire non-propagation according to EN 60332-3 / IEC 60332-3 (grey sheath only)",
            "fr": "Non-propagation de l'incendie selon EN 60332-3 et IEC 60332-3 (gaine grise uniquement)",
            "es": "No propagación del incendio según UNE-EN 60332-3 / IEC 60332-3 (solo cubierta gris)",
        }[lang]),
        make_prop(lang, "cpr", {
            "en": "Cca-s2, d1, a3 (grey 300/500 V) / Cca-s3, d1, a3 (grey 0.6/1 kV) / Eca (black) according to EN 50575",
            "fr": "Cca-s2, d1, a3 (gris 300/500 V) / Cca-s3, d1, a3 (gris 0,6/1 kV) / Eca (noir) selon EN 50575",
            "es": "Cca-s2, d1, a3 (gris 300/500 V) / Cca-s3, d1, a3 (gris 0,6/1 kV) / Eca (negro) según EN 50575",
        }[lang]),
        make_prop(lang, "reduced_halogens", REDUCED_HALOGENS[lang]),
        make_prop(lang, "min_bending", {
            "en": "5x cable diameter",
            "fr": "5x diamètre du câble",
            "es": "5x diámetro exterior",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_GOOD[lang]),
        make_prop(lang, "uv", UV_UNE211605[lang]),
        make_prop(lang, "water", WATER_AD5[lang]),
        make_prop(lang, "installation", INSTALL_FULL[lang]),
        make_prop(lang, "standards_ref", "EN 50525, IEC 60502-1"),
        make_prop(lang, "standards_approvals", "RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Control circuits, Electronic equipment, Signal transmission",
            "fr": "Circuits de contrôle, Équipements électroniques, Transmission de signaux",
            "es": "Circuitos de control, Equipos electrónicos, Transmisión de señal",
        }[lang]),
    ]

CABLE_7 = {
    "common": {
        "slug": "screenflex-110-liycy-vc4v-k",
        "mpn": "LiYCY VC4V-K",
        "brand": "SCREENFLEX®",
        "family": "pvc",
        "datasheet_slug": "screenflex-110-200-liycy-vc4v-k",
        "images": [
            IMG_BASE + "topcable-liycy-vc4v-k-flexible-screened-pvc-cable-for-safe-signal-transmission-01.png",
            IMG_BASE + "TOPCABLE_SCREENFLEX_110_LIYCY_VC4V_K_200_VC4V_K.webp",
            IMG_BASE + "bobina_gris.png"
        ],
    },
    "data": {
        "en": {
            "name": "SCREENFLEX® 110/200 LiYCY VC4V-K",
            "description": "Flexible screened PVC cable, for safe signal transmission. ACCORDING TO: EN 50525 / IEC 60502-1. SCREENFLEX® 110/200 LiYCY VC4V-K is a screened control cable for control circuits, electronic equipment connections, and computer systems. The aluminium-polyester tape screen with tinned copper drain wire provides superior EMI/RFI shielding ensuring signal integrity in electrically noisy environments.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_INDUSTRIAL["en"],
            "properties": cable_screenflex("en"),
        },
        "fr": {
            "name": "SCREENFLEX® 110/200 LiYCY VC4V-K",
            "description": "Câble PVC souple blindé, pour la transmission sécurisée de signaux. SELON : EN 50525 / IEC 60502-1. Le SCREENFLEX® 110/200 LiYCY VC4V-K est un câble de commande blindé pour les circuits de commande, les connexions d'équipements électroniques et les systèmes informatiques. L'écran en bande aluminium-polyester avec drain en cuivre étamé assure un blindage EMI/RFI supérieur garantissant l'intégrité du signal dans les environnements électriquement bruyants.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_INDUSTRIAL["fr"],
            "properties": cable_screenflex("fr"),
        },
        "es": {
            "name": "SCREENFLEX® 110/200 LiYCY VC4V-K",
            "description": "Cable flexible apantallado de PVC, para transmisión segura de señal. NORMAS DE REFERENCIA: EN 50525 / IEC 60502-1. El SCREENFLEX® 110/200 LiYCY VC4V-K es un cable de control apantallado para circuitos de control, conexiones de equipos electrónicos y sistemas informáticos. La pantalla de cinta aluminio-poliéster con drenaje de cobre estañado proporciona un blindaje EMI/RFI superior garantizando la integridad de la señal en entornos eléctricamente ruidosos.",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_INDUSTRIAL["es"],
            "properties": cable_screenflex("es"),
        },
    },
}


# ============================================================
# CABLE 8: TOPFLAT® H05VVH6-F & H07VVH6-F
# ============================================================
def cable_topflat(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "PVC (flexible) according to EN 50214",
            "fr": "PVC (souple) selon EN 50214",
            "es": "PVC (flexible) según EN 50214",
        }[lang]),
        make_prop(lang, "layup", {
            "en": "Insulated conductors placed side by side in parallel arrangement forming flat cable",
            "fr": "Conducteurs isolés placés côte à côte en disposition parallèle formant un câble plat",
            "es": "Conductores aislados colocados lado a lado en disposición paralela formando cable plano",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "PVC (flexible). Black colour. Ripcord for gentle tearing",
            "fr": "PVC (souple). Couleur noire. Cordon de déchirure pour ouverture facile",
            "es": "PVC (flexible). Color negro. Hilo de rasgado para apertura fácil",
        }[lang]),
        make_prop(lang, "rated_voltage", {
            "en": "300/500 V (H05VVH6-F up to 1 mm²) and 450/750 V (H07VVH6-F from 1.5 mm²)",
            "fr": "300/500 V (H05VVH6-F jusqu'à 1 mm²) et 450/750 V (H07VVH6-F à partir de 1,5 mm²)",
            "es": "300/500 V (H05VVH6-F hasta 1 mm²) y 450/750 V (H07VVH6-F desde 1,5 mm²)",
        }[lang]),
        make_prop(lang, "max_temp", "70", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_160[lang], "°C"),
        make_prop(lang, "min_service_temp", {
            "en": "0 (mobile use)",
            "fr": "0 (service mobile)",
            "es": "0 (servicio móvil)",
        }[lang], "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "reduced_halogens", REDUCED_HALOGENS[lang]),
        make_prop(lang, "min_bending", {
            "en": "5x smaller dimension (free movement), 10x smaller dimension (festooned or deflected by pulleys)",
            "fr": "5x plus petite dimension (mouvement libre), 10x plus petite dimension (en guirlande ou par poulies)",
            "es": "5x dimensión menor (movimiento libre), 10x dimensión menor (en guirnalda o por poleas)",
        }[lang]),
        make_prop(lang, "impact", IMPACT_AG2[lang]),
        make_prop(lang, "chemical_oil", CHEM_ACCEPTABLE[lang]),
        make_prop(lang, "water", WATER_AD5[lang]),
        make_prop(lang, "installation", INSTALL_OPEN[lang]),
        make_prop(lang, "standards_ref", "EN 50214"),
        make_prop(lang, "standards_approvals", "HAR, AENOR, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Lifts, Cranes, Hoists, Conveyor systems",
            "fr": "Ascenseurs, Grues, Palans, Systèmes de convoyage",
            "es": "Ascensores, Grúas, Polipastos, Sistemas de transporte",
        }[lang]),
    ]

CABLE_8 = {
    "common": {
        "slug": "topflat-h05vvh6-f-and-h07vvh6-f",
        "slug_fr": "topflat-h05vvh6-f-et-h07vvh6-f",
        "slug_es": "topflat-h05vvh6-f-y-h07vvh6-f",
        "mpn": "H05VVH6-F & H07VVH6-F",
        "brand": "TOPFLAT®",
        "family": "pvc",
        "datasheet_slug": "topflat-h05vvh6-f-h07vvh6-f",
        "images": [
            IMG_BASE + "topcable-h05vvh6-f-h07vvh6-f-flat-cable-for-lifts-cranes-hoists-and-conveyor-systems-01.png",
            IMG_BASE + "TOPCABLE_TOPFLAT_H05VVH6_FH07VVH6_F.webp",
            IMG_BASE + "bobina_negra.png"
        ],
    },
    "data": {
        "en": {
            "name": "TOPFLAT® H05VVH6-F & H07VVH6-F",
            "description": "Flat cable for lifts, cranes, hoists and conveyor systems. ACCORDING TO: EN 50214. TOPFLAT® H05VVH6-F & H07VVH6-F is a flat cable specially designed for cranes, lifts, hoists, drum reeling and conveyor systems. The hanging length can reach up to 35 m and pull out speed up to 1.6 m/s.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_INDUSTRIAL["en"],
            "properties": cable_topflat("en"),
        },
        "fr": {
            "name": "TOPFLAT® H05VVH6-F & H07VVH6-F",
            "description": "Câble plat pour ascenseurs, grues, palans et systèmes de convoyage. SELON : EN 50214. Le TOPFLAT® H05VVH6-F & H07VVH6-F est un câble plat spécialement conçu pour les grues, ascenseurs, palans, enroulements sur tambour et systèmes de convoyage. La longueur suspendue peut atteindre 35 m et la vitesse de déroulement jusqu'à 1,6 m/s.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_INDUSTRIAL["fr"],
            "properties": cable_topflat("fr"),
        },
        "es": {
            "name": "TOPFLAT® H05VVH6-F & H07VVH6-F",
            "description": "Cable plano para ascensores, grúas, polipastos y sistemas de transporte. NORMAS DE REFERENCIA: EN 50214. El TOPFLAT® H05VVH6-F & H07VVH6-F es un cable plano especialmente diseñado para grúas, ascensores, polipastos, enrollado en tambor y sistemas de transporte. La longitud suspendida puede alcanzar 35 m y la velocidad de extracción hasta 1,6 m/s.",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_INDUSTRIAL["es"],
            "properties": cable_topflat("es"),
        },
    },
}


# ============================================================
# CABLE 9: SIWO XTREM®
# ============================================================
def cable_siwo(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_TINNED_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "Silicone rubber according to IEC 60502-1",
            "fr": "Caoutchouc silicone selon IEC 60502-1",
            "es": "Caucho de silicona según IEC 60502-1",
        }[lang]),
        make_prop(lang, "outer_sheath", {
            "en": "Protective synthetic yarn braid, PUR varnished. Yellow colour (1.1 kV), Red colour (3.3 kV)",
            "fr": "Tresse de fils synthétiques protectrice, vernie PUR. Couleur jaune (1,1 kV), Couleur rouge (3,3 kV)",
            "es": "Trenzado protector de hilos sintéticos, barnizado PUR. Color amarillo (1,1 kV), Color rojo (3,3 kV)",
        }[lang]),
        make_prop(lang, "rated_voltage", {
            "en": "1.1 kV and 3.3 kV",
            "fr": "1,1 kV et 3,3 kV",
            "es": "1,1 kV y 3,3 kV",
        }[lang]),
        make_prop(lang, "max_temp", "180", "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "fire_nonprop", FIRE_NONPROP_3_24[lang]),
        make_prop(lang, "fire_resistant", {
            "en": "Fire resistant (PH120) minimum 120 minutes at 840°C according to IEC 60331-2 / EN 50200 (cable diameter ≤ 20 mm) and IEC 60331-1 / EN 50362 (cable diameter > 20 mm)",
            "fr": "Résistance au feu (PH120) minimum 120 minutes à 840°C selon IEC 60331-2 / EN 50200 (diamètre câble ≤ 20 mm) et IEC 60331-1 / EN 50362 (diamètre câble > 20 mm)",
            "es": "Resistencia al fuego (PH120) mínimo 120 minutos a 840°C según IEC 60331-2 / EN 50200 (diámetro cable ≤ 20 mm) e IEC 60331-1 / EN 50362 (diámetro cable > 20 mm)",
        }[lang]),
        make_prop(lang, "halogen_free", HALOGEN_FREE[lang]),
        make_prop(lang, "low_corrosive_gases", LOW_CORROSIVE_GASES[lang]),
        make_prop(lang, "low_smoke", LOW_SMOKE_61034[lang]),
        make_prop(lang, "light_transmittance", "> 60%"),
        make_prop(lang, "min_bending", {
            "en": "5x cable diameter",
            "fr": "5x diamètre du câble",
            "es": "5x diámetro del cable",
        }[lang]),
        make_prop(lang, "chemical_oil", CHEM_EXCELLENT[lang]),
        make_prop(lang, "installation", {
            "en": "Fixed installations",
            "fr": "Installations fixes",
            "es": "Instalaciones fijas",
        }[lang]),
        make_prop(lang, "standards_ref", "IEC 60502-1"),
        make_prop(lang, "standards_approvals", "RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Wind converters, Transformers, Solar power inverters, Drives",
            "fr": "Convertisseurs éoliens, Transformateurs, Onduleurs solaires, Variateurs",
            "es": "Convertidores eólicos, Transformadores, Inversores solares, Variadores",
        }[lang]),
    ]

CABLE_9 = {
    "common": {
        "slug": "siwo-xtrem",
        "mpn": "SIWO XTREM",
        "brand": "SIWO XTREM®",
        "family": "lszh",
        "datasheet_slug": "siwo-xtrem",
        "images": [
            IMG_BASE + "topcable-high-temperature-and-fire-resistant-power-cable-01.webp",
            IMG_BASE + "TOPCABLE_SIWO_XTREM.webp",
            IMG_BASE + "bobina_negra.png"
        ],
    },
    "data": {
        "en": {
            "name": "SIWO XTREM®",
            "description": "High temperature and fire resistant power cable. ACCORDING TO: IEC 60502-1. SIWO XTREM® is a fire resistant cable designed for high temperature conditions. The silicone rubber insulation and PUR varnished synthetic yarn braid outer sheath provide excellent chemical resistance and dielectric strength. Suitable for wind converters, transformers, solar power inverters and drives.",
            "material": MATERIAL_TINNED_COPPER_FLEX["en"],
            "audience": AUDIENCE_INDUSTRIAL["en"],
            "properties": cable_siwo("en"),
        },
        "fr": {
            "name": "SIWO XTREM®",
            "description": "Câble d'alimentation haute température et résistant au feu. SELON : IEC 60502-1. Le SIWO XTREM® est un câble résistant au feu conçu pour les conditions de haute température. L'isolation en caoutchouc silicone et la gaine extérieure en tresse de fils synthétiques vernie PUR offrent une excellente résistance chimique et rigidité diélectrique. Adapté aux convertisseurs éoliens, transformateurs, onduleurs solaires et variateurs.",
            "material": MATERIAL_TINNED_COPPER_FLEX["fr"],
            "audience": AUDIENCE_INDUSTRIAL["fr"],
            "properties": cable_siwo("fr"),
        },
        "es": {
            "name": "SIWO XTREM®",
            "description": "Cable de potencia de alta temperatura y resistente al fuego. NORMAS DE REFERENCIA: IEC 60502-1. El SIWO XTREM® es un cable resistente al fuego diseñado para condiciones de alta temperatura. El aislamiento de caucho de silicona y la cubierta exterior de trenzado de hilos sintéticos barnizado PUR proporcionan una excelente resistencia química y rigidez dieléctrica. Adecuado para convertidores eólicos, transformadores, inversores solares y variadores.",
            "material": MATERIAL_TINNED_COPPER_FLEX["es"],
            "audience": AUDIENCE_INDUSTRIAL["es"],
            "properties": cable_siwo("es"),
        },
    },
}


# ============================================================
# CABLE 10: TOXFREE® LSZH MX
# ============================================================
def cable_mx(lang):
    return [
        make_prop(lang, "conductor", CONDUCTOR_COPPER_FLEX[lang], url=ELECTROPEDIA_URL),
        make_prop(lang, "insulation", {
            "en": "Rubber LSZH according to IEC 60092-353",
            "fr": "Caoutchouc LSZH selon IEC 60092-353",
            "es": "Caucho LSZH según IEC 60092-353",
        }[lang]),
        make_prop(lang, "rated_voltage", "0.6/1", "kV"),
        make_prop(lang, "max_temp", "90", "°C"),
        make_prop(lang, "max_sc_temp", SC_TEMP_250[lang], "°C"),
        make_prop(lang, "min_service_temp", MIN_TEMP_FIXED[lang], "°C"),
        make_prop(lang, "flame_nonprop", FLAME_NONPROP[lang]),
        make_prop(lang, "fire_nonprop", FIRE_NONPROP_3_22[lang]),
        make_prop(lang, "halogen_free", HALOGEN_FREE[lang]),
        make_prop(lang, "low_corrosive_gases", LOW_CORROSIVE_GASES[lang]),
        make_prop(lang, "low_smoke", LOW_SMOKE_61034[lang]),
        make_prop(lang, "light_transmittance", "> 60%"),
        make_prop(lang, "min_bending", {
            "en": "4x cable diameter",
            "fr": "4x diamètre du câble",
            "es": "4x diámetro del cable",
        }[lang]),
        make_prop(lang, "chemical_oil", CHEM_ACCEPTABLE[lang]),
        make_prop(lang, "installation", {
            "en": "Open Air. In conduit on bulkhead. On bulkhead.",
            "fr": "À l'air libre. En canalisation sur cloison. Sur cloison.",
            "es": "Al aire. Entubado en mamparo. En mamparo.",
        }[lang]),
        make_prop(lang, "standards_ref", "IEC 60092-353"),
        make_prop(lang, "standards_approvals", "DNV-GL, RoHS, CE"),
        make_prop(lang, "applications", {
            "en": "Marine vessels, Fishing vessels, Cruise ships & Yachts",
            "fr": "Navires, Bateaux de pêche, Navires de croisière et yachts",
            "es": "Embarcaciones, Barcos de pesca, Cruceros y yates",
        }[lang]),
    ]

CABLE_10 = {
    "common": {
        "slug": "toxfree-lszh-mx",
        "mpn": "MX",
        "brand": "TOXFREE®",
        "family": "lszh",
        "datasheet_slug": "toxfree-lszh-mx",
        "images": [
            IMG_BASE + "topcable-mx-flexible-and-halogen-free-90c-cable-for-marine-applications-01.png",
            IMG_BASE + "TOPCABLE_TOXFREE_LSZH_MX.webp",
            IMG_BASE + "bobina_negra.png"
        ],
    },
    "data": {
        "en": {
            "name": "TOXFREE® LSZH MX",
            "description": "Flexible and halogen free 90°C cable for marine applications. ACCORDING TO: IEC 60092-353. TOXFREE® LSZH MX is a flexible cable for fixed and protected installations. It is highly recommended in marine applications and for use in public places. Suitable for power, control, and instrumentation applications on fishing vessels, merchant vessels, cruise ships and yachts. DNV-GL certified.",
            "material": MATERIAL_COPPER_FLEX["en"],
            "audience": AUDIENCE_MARINE["en"],
            "properties": cable_mx("en"),
        },
        "fr": {
            "name": "TOXFREE® LSZH MX",
            "description": "Câble souple et sans halogène 90°C pour applications marines. SELON : IEC 60092-353. Le TOXFREE® LSZH MX est un câble souple pour installations fixes et protégées. Il est fortement recommandé pour les applications marines et l'utilisation dans les lieux publics. Adapté aux applications de puissance, contrôle et instrumentation sur les bateaux de pêche, navires marchands, navires de croisière et yachts. Certifié DNV-GL.",
            "material": MATERIAL_COPPER_FLEX["fr"],
            "audience": AUDIENCE_MARINE["fr"],
            "properties": cable_mx("fr"),
        },
        "es": {
            "name": "TOXFREE® LSZH MX",
            "description": "Cable flexible y libre de halógenos 90°C para aplicaciones marinas. NORMAS DE REFERENCIA: IEC 60092-353. El TOXFREE® LSZH MX es un cable flexible para instalaciones fijas y protegidas. Altamente recomendado para aplicaciones marinas y uso en lugares públicos. Adecuado para aplicaciones de potencia, control e instrumentación en barcos de pesca, buques mercantes, cruceros y yates. Certificado DNV-GL.",
            "material": MATERIAL_COPPER_FLEX["es"],
            "audience": AUDIENCE_MARINE["es"],
            "properties": cable_mx("es"),
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
