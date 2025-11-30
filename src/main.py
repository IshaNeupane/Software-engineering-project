from assignment import Assignment
from similarityEngine import SimilarityEngine

# Create two fake assignments
a1 = Assignment()
a1.content = "print('Hello world')"

a2 = Assignment()
a2.content = "print('Hello World!')"

engine = SimilarityEngine()
score = engine.calculateSimilarity(a1, a2)

print("Similarity Score:", score)
