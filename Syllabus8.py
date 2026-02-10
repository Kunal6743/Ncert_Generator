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


# ================= CLASS 8 – FULL DEEP NCERT DATA =================
data = [

# ================= CLASS 8 – SCIENCE =================
(8,"Science",1,"Crop Production and Management",
"Agricultural practices; Preparation of soil (ploughing, levelling); "
"Sowing methods and selection of seeds; Manure and fertilizers with differences; "
"Irrigation methods (traditional and modern); Protection from weeds; "
"Harvesting and storage of crops; Food from animals; "
"Reasons for use of modern agricultural practices"),

(8,"Science",2,"Microorganisms: Friend and Foe",
"Definition of microorganisms; Types (bacteria, fungi, protozoa, algae, viruses); "
"Useful microorganisms (food production, medicines, nitrogen fixation); "
"Harmful microorganisms and diseases; Food preservation methods; "
"Role of microorganisms in nitrogen cycle"),

(8,"Science",3,"Synthetic Fibres and Plastics",
"Synthetic fibres (rayon, nylon, polyester, acrylic); "
"Properties of synthetic fibres; Plastics and their types (thermoplastics, thermosetting); "
"Characteristics of plastics; Uses and disadvantages of plastics; "
"Environmental impact and non-biodegradability"),

(8,"Science",4,"Materials: Metals and Non-metals",
"Physical properties of metals and non-metals; "
"Chemical properties and reactions; Uses of metals and non-metals; "
"Corrosion and prevention; Reactivity series (introductory); "
"Everyday applications"),

(8,"Science",5,"Coal and Petroleum",
"Natural resources; Fossil fuels; Coal and its products (coke, coal tar, coal gas); "
"Petroleum refining; Petrochemical products; Non-renewable resources; "
"Conservation of fossil fuels"),

(8,"Science",6,"Combustion and Flame",
"Combustion process; Conditions for combustion; Types of combustion; "
"Flame structure; Characteristics of a good fuel; "
"Harmful effects of burning fuels"),

(8,"Science",7,"Conservation of Plants and Animals",
"Deforestation causes and consequences; Conservation of forests and wildlife; "
"Biosphere reserves; National parks and sanctuaries; "
"Endangered species; Migration; Recycling of paper"),

(8,"Science",8,"Cell – Structure and Functions",
"Discovery of cell; Cell theory; Structure of plant and animal cell; "
"Cell organelles and their functions; Comparison of plant and animal cells"),

(8,"Science",9,"Reproduction in Animals",
"Modes of reproduction (sexual and asexual); Male and female reproductive organs; "
"Fertilisation and its types; Development of embryo; "
"Viviparous and oviparous animals"),

(8,"Science",10,"Reaching the Age of Adolescence",
"Adolescence and puberty; Physical and mental changes; "
"Role of hormones; Secondary sexual characteristics; "
"Reproductive health and hygiene"),

(8,"Science",11,"Force and Pressure",
"Force and its effects; Contact and non-contact forces; "
"Pressure definition and applications; Atmospheric pressure; "
"Daily life examples"),

(8,"Science",12,"Friction",
"Friction and its causes; Types of friction; "
"Advantages and disadvantages of friction; "
"Methods to increase or reduce friction"),

(8,"Science",13,"Sound",
"Production of sound; Propagation of sound waves; "
"Characteristics of sound (amplitude, frequency, pitch); "
"Audible and inaudible sounds; Noise pollution"),

(8,"Science",14,"Chemical Effects of Electric Current",
"Conductors and insulators; Chemical effects of electric current; "
"Electroplating process; Applications of electroplating"),

(8,"Science",15,"Some Natural Phenomena",
"Lightning and its causes; Charging by friction; "
"Earthquakes and safety measures; "
"Natural disaster preparedness"),

(8,"Science",16,"Light",
"Reflection of light; Laws of reflection; "
"Multiple reflection; Applications of mirrors; "
"Periscope and kaleidoscope"),

(8,"Science",17,"Stars and the Solar System",
"Celestial bodies; Solar system; "
"Planets and their characteristics; "
"Constellations; Phases of the moon"),

(8,"Science",18,"Pollution of Air and Water",
"Air pollution causes and effects; Water pollution causes and effects; "
"Methods to control pollution; Potable water; "
"Government initiatives"),

# ================= CLASS 8 – MATHEMATICS =================
(8,"Mathematics",1,"Rational Numbers",
"Definition of rational numbers; Properties of rational numbers; "
"Representation on number line"),

(8,"Mathematics",2,"Linear Equations in One Variable",
"Formation of linear equations; Solving linear equations; "
"Word problems based on linear equations"),

(8,"Mathematics",3,"Understanding Quadrilaterals",
"Polygons; Types of quadrilaterals; "
"Angle sum property; Properties of special quadrilaterals"),

(8,"Mathematics",4,"Practical Geometry",
"Construction of quadrilaterals; Conditions for construction"),

(8,"Mathematics",5,"Data Handling",
"Collection of data; Mean, median and mode; "
"Graphical representation; Probability basics"),

(8,"Mathematics",6,"Squares and Square Roots",
"Perfect squares; Properties of square numbers; "
"Finding square roots"),

(8,"Mathematics",7,"Cubes and Cube Roots",
"Perfect cubes; Cube roots and methods"),

(8,"Mathematics",8,"Comparing Quantities",
"Percentage; Increase and decrease percentage; "
"Profit and loss; Discount; Simple interest"),

(8,"Mathematics",9,"Algebraic Expressions",
"Terms and coefficients; Like and unlike terms; "
"Simplification of expressions"),

(8,"Mathematics",10,"Visualising Solid Shapes",
"3D objects; Nets; Views of solids"),

(8,"Mathematics",11,"Mensuration",
"Area of plane figures; Surface area and volume; "
"Applications in daily life"),

(8,"Mathematics",12,"Exponents and Powers",
"Laws of exponents; Standard form of numbers"),

(8,"Mathematics",13,"Direct and Inverse Proportions",
"Direct proportion; Inverse proportion; "
"Applications"),

(8,"Mathematics",14,"Factorisation",
"Factorisation methods; Identity based factorisation"),

(8,"Mathematics",15,"Introduction to Graphs",
"Coordinate plane; Plotting points; "
"Reading graphs"),

(8,"Mathematics",16,"Playing with Numbers",
"Divisibility rules; Logical reasoning; "
"Patterns in numbers")
]

# ================= INSERT INTO DATABASE =================
cur.executemany("""
INSERT INTO chapters ("class", subject, chapter_no, chapter_name, key_topics)VALUES (?, ?, ?, ?, ?)""", data)

conn.commit()
conn.close()

print("✅ Class 8 (Science + Mathematics) FULL DEEP NCERT syllabus inserted successfully")