 import streamlit as st

st.set_page_config(page_title="Anatomy AI Tutor")

st.title("Anatomy AI Tutor")
st.write("Ask about: Heart, Brain, Lungs, Liver, or Kidneys")

question = st.text_input("Ask your question:")


def anatomy_response(user_input):
    user_input = user_input.lower()

    if "heart" in user_input:
        return """
HEART

The heart is a hollow, muscular organ responsible for pumping blood 
throughout the circulatory system. It maintains continuous blood flow 
to deliver oxygen and nutrients to tissues and remove carbon dioxide.

Location:
- Middle mediastinum of the thoracic cavity
- Slightly tilted toward the left side

Structure:
- Four chambers:
    • Right Atrium
    • Right Ventricle
    • Left Atrium
    • Left Ventricle
- Septum separates right and left sides
- Valves:
    • Tricuspid valve
    • Pulmonary valve
    • Mitral (Bicuspid) valve
    • Aortic valve

Circulation:
- Pulmonary circulation (Heart ↔ Lungs)
- Systemic circulation (Heart ↔ Body)

Electrical System:
- SA node (natural pacemaker)
- AV node
- Bundle of His
- Purkinje fibers

Major Blood Vessels:
- Aorta
- Pulmonary arteries
- Pulmonary veins
- Superior vena cava
- Inferior vena cava
"""

    elif "brain" in user_input:
        return """
BRAIN

The brain is the central control organ of the nervous system.
It regulates voluntary and involuntary functions and enables cognition.

Location:
- Cranial cavity
- Protected by skull, meninges, and cerebrospinal fluid

Major Parts:

Cerebrum:
- Largest part of the brain
- Controls thinking, memory, speech, voluntary movement
- Divided into frontal, parietal, temporal, and occipital lobes

Cerebellum:
- Coordinates balance
- Controls fine motor movement

Brainstem:
- Includes midbrain, pons, medulla oblongata
- Controls breathing, heart rate, reflexes

Protection:
- Skull
- Meninges (Dura mater, Arachnoid mater, Pia mater)
- Cerebrospinal fluid
"""

    elif "lungs" in user_input:
        return """
LUNGS

The lungs are paired respiratory organs responsible for gas exchange.

Location:
- Thoracic cavity
- Protected by rib cage
- Right lung has 3 lobes
- Left lung has 2 lobes

Airway Structure:
- Trachea
- Bronchi
- Bronchioles
- Alveoli (site of gas exchange)

Gas Exchange:
- Oxygen diffuses into blood
- Carbon dioxide diffuses out
- Occurs at the alveolar-capillary membrane

Additional Information:
- Surfactant prevents alveolar collapse
- Maintains blood pH balance
"""

    elif "liver" in user_input:
        return """
LIVER

The liver is the largest internal organ and a major metabolic center.

Location:
- Upper right quadrant of abdomen
- Below diaphragm

Structure:
- Right and left lobes
- Made of hepatic lobules
- Functional cells called hepatocytes

Functions:
- Detoxification of drugs and toxins
- Metabolism of carbohydrates, fats, and proteins
- Storage of glycogen
- Production of bile
- Synthesis of clotting factors

Blood Supply:
- Hepatic artery (oxygen-rich blood)
- Portal vein (nutrient-rich blood)

Additional Role:
- Immune defense via Kupffer cells
"""

    elif "kidney" in user_input or "kidneys" in user_input:
        return """
KIDNEYS

The kidneys are bean-shaped organs responsible for filtration 
and maintaining internal balance (homeostasis).

Location:
- Retroperitoneal space
- On either side of vertebral column

Structure:
- Renal cortex
- Renal medulla
- Renal pelvis

Functional Unit:
- Nephron
    • Glomerulus (filtration)
    • Bowman’s capsule
    • Loop of Henle
    • Collecting duct

Functions:
- Removes nitrogenous wastes
- Regulates electrolyte balance
- Controls blood pressure (Renin)
- Produces erythropoietin (RBC production)
- Maintains acid-base balance

Produces urine for excretion
"""

    else:
        return "Please ask about Heart, Brain, Lungs, Liver, or Kidneys."


if question:
    answer = anatomy_response(question)
    st.success(answer)
