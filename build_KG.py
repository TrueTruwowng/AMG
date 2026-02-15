from AMG_with_KG import AMG_RAG_System
import json
from dataclasses import asdict
# Initialize the system
system = AMG_RAG_System(use_openai=True,openai_key=)

# Sample medical question
question_data = {
    "question": "A 45-year-old man presents with severe chest pain...",
    "options": {
        "A": "Unstable angina",
        "B": "Acute inferior wall myocardial infarction",
        "C": "Acute anterior wall myocardial infarction",
        "D": "Aortic dissection",
        "E": "Pulmonary embolism"
    },
    "answer": "B"
}

# Get answer with reasoning
result = system.answer_question(question_data)

print(f"Answer: {result['answer']}")
print(f"Confidence: {result['confidence']:.2f}")
print(f"Explanation: {result['explanation']}")
# Access the knowledge graph
kg = system.kg

# Explore entities
for entity_name, entity in kg.entities.items():
    print(f"Entity: {entity_name}")
    print(f"Type: {entity.entity_type}")
    print(f"Confidence: {entity.confidence:.2f}")
    print(f"Description: {entity.description[:100]}...")

# Explore relationships
for relation in kg.relations:
    print(f"{relation.source} --[{relation.relation_type}]--> {relation.target}")
    print(f"Confidence: {relation.confidence:.2f}")

result = system.answer_question(question_data)
