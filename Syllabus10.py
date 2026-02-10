import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "ncert_syllabus.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS chapters (
    chapter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    "class" INTEGER,
    subject TEXT,
    chapter_no INTEGER,
    chapter_name TEXT,
    key_topics TEXT
)
""")

conn.commit() 


# ================= CLASS 10 – FULL DEEP NCERT DATA =================
data = [

# ================= CLASS 10 – SCIENCE =================
(10,"Science",1,"Chemical Reactions and Equations",
"Chemical reactions and chemical equations; "
"Writing word equations and skeletal equations; "
"Balancing chemical equations; "
"Types of chemical reactions "
"(combination, decomposition, displacement, double displacement, redox reactions); "
"Effects of oxidation and reduction in daily life; "
"Corrosion and its prevention; "
"Rancidity and methods to prevent it"),

(10,"Science",2,"Acids, Bases and Salts",
"Acids, bases and salts definitions; "
"Chemical properties of acids, bases and salts; "
"pH scale and its importance; "
"Strength of acids and bases; "
"Common salts (washing soda, baking soda, plaster of Paris); "
"Uses of acids, bases and salts in daily life"),

(10,"Science",3,"Metals and Non-metals",
"Physical properties of metals and non-metals; "
"Chemical properties of metals and non-metals; "
"Reactivity series; "
"Extraction of metals; "
"Corrosion and its prevention; "
"Uses of metals and non-metals"),

(10,"Science",4,"Carbon and its Compounds",
"Covalent bonding; "
"Allotropes of carbon; "
"Hydrocarbons (saturated and unsaturated); "
"Homologous series; "
"Functional groups; "
"Ethanol and ethanoic acid; "
"Soaps and detergents"),

(10,"Science",5,"Life Processes",
"Life processes and their importance; "
"Nutrition in plants and animals; "
"Respiration (aerobic and anaerobic); "
"Transportation in plants and animals; "
"Excretion in human beings"),

(10,"Science",6,"Control and Coordination",
"Nervous system and its parts; "
"Reflex action and reflex arc; "
"Hormones and endocrine glands; "
"Coordination in plants; "
"Difference between nervous and hormonal control"),

(10,"Science",7,"How do Organisms Reproduce",
"Modes of reproduction (asexual and sexual); "
"Reproduction in human beings; "
"Male and female reproductive systems; "
"Reproductive health; "
"Birth control methods"),

(10,"Science",8,"Heredity and Evolution",
"Heredity and inheritance; "
"Mendel’s experiments; "
"Genotype and phenotype; "
"Traits and variations; "
"Acquired and inherited traits; "
"Evolution and speciation"),

(10,"Science",9,"Light – Reflection and Refraction",
"Reflection of light; "
"Laws of reflection; "
"Spherical mirrors and their uses; "
"Image formation by mirrors; "
"Refraction of light; "
"Refraction through glass slab; "
"Ray diagrams and numerical problems"),

(10,"Science",10,"The Human Eye and the Colourful World",
"Structure and function of human eye; "
"Defects of vision and their correction; "
"Dispersion of light; "
"Scattering of light; "
"Applications in daily life"),

(10,"Science",11,"Electricity",
"Electric current and electric circuit; "
"Electric potential difference; "
"Ohm’s Law and V–I graph; "
"Resistance and factors affecting resistance; "
"Series and parallel combination of resistors; "
"Electric power; "
"Commercial unit of electrical energy; "
"Numerical problems"),

(10,"Science",12,"Magnetic Effects of Electric Current",
"Magnetic field and magnetic field lines; "
"Right hand thumb rule; "
"Fleming’s left hand rule; "
"Fleming’s right hand rule; "
"Electromagnetic induction; "
"Electric motor and electric generator; "
"Alternating current and direct current"),

(10,"Science",13,"Our Environment",
"Ecosystem and its components; "
"Food chains and food webs; "
"Trophic levels; "
"Energy flow in an ecosystem; "
"Biological magnification"),

(10,"Science",14,"Sources of Energy",
"Renewable and non-renewable sources of energy; "
"Thermal power plants; "
"Solar energy; Wind energy; Hydro power; "
"Biogas plant; "
"Advantages and disadvantages of various energy sources"),

(10,"Science",15,"Management of Natural Resources",
"Management of natural resources; "
"Conservation of forests and wildlife; "
"Case study of dams; "
"Sustainable use of resources"),

# ================= CLASS 10 – MATHEMATICS =================
(10,"Mathematics",1,"Real Numbers",
"Euclid’s division lemma; "
"Fundamental theorem of arithmetic; "
"HCF and LCM; "
"Proofs based on Euclid’s lemma"),

(10,"Mathematics",2,"Polynomials",
"Zeros of a polynomial; "
"Relationship between zeros and coefficients; "
"Graphical representation of polynomials"),

(10,"Mathematics",3,"Pair of Linear Equations in Two Variables",
"Pair of linear equations; "
"Graphical method of solution; "
"Algebraic methods (substitution and elimination); "
"Consistency of equations; "
"Word problems"),

(10,"Mathematics",4,"Quadratic Equations",
"Standard form of quadratic equations; "
"Methods of solving quadratic equations "
"(factorisation, completing square, quadratic formula); "
"Nature of roots using discriminant; "
"Word problems"),

(10,"Mathematics",5,"Arithmetic Progressions",
"Definition of arithmetic progression; "
"nth term of an AP; "
"Sum of first n terms; "
"Word problems"),

(10,"Mathematics",6,"Triangles",
"Similarity of triangles; "
"Criteria for similarity of triangles; "
"Pythagoras theorem and its applications"),

(10,"Mathematics",7,"Coordinate Geometry",
"Distance formula; "
"Section formula; "
"Area of a triangle using coordinates"),

(10,"Mathematics",8,"Introduction to Trigonometry",
"Trigonometric ratios; "
"Values of trigonometric ratios; "
"Trigonometric identities and proofs"),

(10,"Mathematics",9,"Applications of Trigonometry",
"Heights and distances; "
"Angle of elevation and angle of depression"),

(10,"Mathematics",10,"Circles",
"Tangent to a circle; "
"Number of tangents from a point; "
"Theorems related to tangents"),

(10,"Mathematics",11,"Constructions",
"Division of a line segment; "
"Construction of similar triangles"),

(10,"Mathematics",12,"Areas Related to Circles",
"Areas of sectors and segments of circles; "
"Numerical problems"),

(10,"Mathematics",13,"Surface Areas and Volumes",
"Surface area and volume of solids; "
"Combination of solids; "
"Frustum of a cone"),

(10,"Mathematics",14,"Statistics",
"Mean by step deviation method; "
"Cumulative frequency; "
"Ogive curves"),

(10,"Mathematics",15,"Probability",
"Theoretical probability; "
"Probability of events")
]

# ================= INSERT INTO DATABASE =================
cur.executemany("""
INSERT INTO chapters ("class", subject, chapter_no, chapter_name, key_topics)VALUES (?, ?, ?, ?, ?)""", data)

conn.commit()
conn.close()

print("✅ Class 10 (Science + Mathematics) FULL DEEP NCERT syllabus inserted successfully")
