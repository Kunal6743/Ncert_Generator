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

# ================= CLASS 9 – FULL DEEP NCERT DATA =================
data = [

# ================= CLASS 9 – SCIENCE =================
(9,"Science",1,"Matter in Our Surroundings",
"Definition of matter; Physical nature of matter; Characteristics of particles of matter "
"(inter-particle space, inter-particle force, motion of particles); "
"States of matter (solid, liquid, gas); Diffusion and factors affecting diffusion; "
"Change of state (melting, freezing, boiling, condensation, sublimation); "
"Effect of temperature and pressure; Latent heat; "
"Evaporation and cooling effect with daily life examples"),

(9,"Science",2,"Is Matter Around Us Pure",
"Pure substances and mixtures; Types of mixtures; "
"Solutions and their properties; Concentration of solutions; "
"Suspensions and colloids with differences; "
"Physical and chemical changes; Separation techniques "
"(filtration, evaporation, distillation, chromatography); "
"Applications in daily life"),

(9,"Science",3,"Atoms and Molecules",
"Laws of chemical combination (law of conservation of mass, law of constant proportions); "
"Dalton’s atomic theory and postulates; Atomic mass and molecular mass; "
"Mole concept and numerical problems; Chemical formulae; "
"Balancing chemical equations"),

(9,"Science",4,"Structure of the Atom",
"Discovery of subatomic particles; Thomson’s model of atom; "
"Rutherford’s nuclear model; Bohr’s model of atom; "
"Electronic configuration; Valency; "
"Atomic number and mass number; Isotopes and isobars"),

(9,"Science",5,"The Fundamental Unit of Life",
"Discovery of cell; Cell theory; Structure of plant cell and animal cell; "
"Cell organelles and their functions; "
"Comparison between plant and animal cells"),

(9,"Science",6,"Tissues",
"Definition of tissues; Plant tissues (meristematic and permanent tissues); "
"Animal tissues (epithelial, connective, muscular, nervous); "
"Functions of different tissues"),

(9,"Science",7,"Diversity in Living Organisms",
"Basis of classification; Hierarchy of classification; "
"Five kingdom classification; Binomial nomenclature; "
"Major groups of plants and animals"),

(9,"Science",8,"Motion",
"Distance and displacement; Speed and velocity; Acceleration; "
"Uniform and non-uniform motion; "
"Equations of motion; Graphical representation of motion"),

(9,"Science",9,"Force and Laws of Motion",
"Force and its types; Balanced and unbalanced forces; "
"Newton’s laws of motion; Momentum; "
"Law of conservation of momentum; "
"Applications in daily life"),

(9,"Science",10,"Gravitation",
"Universal law of gravitation; Free fall; "
"Thrust and pressure; Buoyancy; "
"Archimedes’ principle; "
"Applications and numerical problems"),

(9,"Science",11,"Work and Energy",
"Work and its definition; Energy and its forms; "
"Kinetic energy and potential energy; "
"Law of conservation of energy; "
"Power and its units"),

(9,"Science",12,"Sound",
"Production of sound; Propagation of sound waves; "
"Characteristics of sound (amplitude, frequency, pitch); "
"Speed of sound in different media; "
"Echo and reverberation; "
"Audible and inaudible sounds"),

(9,"Science",13,"Why Do We Fall Ill",
"Health and its significance; Acute and chronic diseases; "
"Causes of diseases; Infectious and non-infectious diseases; "
"Prevention and treatment of diseases"),

(9,"Science",14,"Natural Resources",
"Natural resources and their types; "
"Renewable and non-renewable resources; "
"Biogeochemical cycles (water, carbon, nitrogen); "
"Conservation of natural resources"),

(9,"Science",15,"Improvement in Food Resources",
"Crop yield improvement methods; "
"Manure and fertilizers; "
"Irrigation methods; Cropping patterns; "
"Animal husbandry; Fisheries and poultry farming"),

# ================= CLASS 9 – MATHEMATICS =================
(9,"Mathematics",1,"Number Systems",
"Real numbers; Rational and irrational numbers; "
"Decimal expansion of real numbers; "
"Laws of exponents for real numbers"),

(9,"Mathematics",2,"Polynomials",
"Definition of polynomial; Degree of polynomial; "
"Zeros of a polynomial; "
"Relationship between zeros and coefficients; "
"Remainder theorem and factor theorem"),

(9,"Mathematics",3,"Coordinate Geometry",
"Cartesian coordinate system; "
"Plotting of points in the plane; "
"Quadrants and coordinate axes"),

(9,"Mathematics",4,"Linear Equations in Two Variables",
"Linear equations in two variables; "
"Graphical representation of linear equations; "
"Solutions of linear equations"),

(9,"Mathematics",5,"Introduction to Euclid’s Geometry",
"Euclid’s definitions; Axioms and postulates; "
"Equivalent versions of Euclid’s axioms"),

(9,"Mathematics",6,"Lines and Angles",
"Intersecting lines; Pairs of angles; "
"Parallel lines and a transversal; "
"Angle sum property and angle relationships"),

(9,"Mathematics",7,"Triangles",
"Congruence of triangles; "
"Criteria for congruence (SSS, SAS, ASA, RHS); "
"Properties of triangles"),

(9,"Mathematics",8,"Quadrilaterals",
"Angle sum property of quadrilaterals; "
"Properties of parallelograms; "
"Theorems on quadrilaterals"),

(9,"Mathematics",9,"Areas of Parallelograms and Triangles",
"Figures on same base and between same parallels; "
"Area theorems; "
"Applications"),

(9,"Mathematics",10,"Circles",
"Circle and related terms; "
"Chord of a circle; "
"Perpendicular from centre to a chord; "
"Angle subtended by a chord at a point"),

(9,"Mathematics",11,"Constructions",
"Basic geometrical constructions; "
"Construction of triangles using given conditions"),

(9,"Mathematics",12,"Heron’s Formula",
"Heron’s formula; "
"Area of triangles using Heron’s formula; "
"Numerical problems"),

(9,"Mathematics",13,"Surface Areas and Volumes",
"Surface area and volume of cubes, cuboids, spheres, cylinders and cones; "
"Applications in daily life"),

(9,"Mathematics",14,"Statistics",
"Collection of data; "
"Representation of data; "
"Mean of grouped and ungrouped data"),

(9,"Mathematics",15,"Probability",
"Experimental probability; "
"Outcomes and events; "
"Simple probability problems")
]

# ================= INSERT INTO DATABASE =================
cur.executemany("""
INSERT INTO chapters ("class", subject, chapter_no, chapter_name, key_topics)VALUES (?, ?, ?, ?, ?)""", data)

conn.commit()
conn.close()

print("✅ Class 9 (Science + Mathematics) FULL DEEP NCERT syllabus inserted successfully")
