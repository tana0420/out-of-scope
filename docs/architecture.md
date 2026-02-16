# System Architecture

## High-Level Architecture

User → Mobile Camera → Vuforia Image Recognition → Unity Engine → 3D Organ Model → User Interaction

## Components
1. **User Interface**
   - Touch gestures for rotate, zoom, pan

2. **Image Recognition**
   - Textbook image used as AR marker
   - Detected using Vuforia SDK

3. **Rendering Engine**
   - Unity renders 3D anatomical models

4. **Interaction Layer**
   - Enables real-time manipulation of organs
