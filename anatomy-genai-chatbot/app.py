def anatomy_response(user_input):
    user_input = user_input.lower()

    if "heart" in user_input:
        return """
         HEART:

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
        - Pulmonary circulation → Heart ↔ Lungs
        - Systemic circulation → Heart ↔ Body

        Electrical System:
        - SA node (natural pacemaker)
        - AV node
        - Bundle of His & Purkinje fibers

        Major Blood Vessels:
        - Aorta
        - Pulmonary arteries
        - Pulmonary veins
        - Superior & Inferior vena cava
        """

    elif "brain" in user_input:
        return """
         BRAIN:

        The brain is the central control organ of the nervous system. 
        It regulates voluntary and involuntary functions and enables cognition.

         Location:
        - Cranial cavity
        - Protected by skull, meninges, and cerebrospinal fluid

         Major Parts:
        1. Cerebrum:
            • Largest part
            • Controls thinking, memory, speech, voluntary movement
            • Divided into frontal, parietal, temporal, occipital lobes
