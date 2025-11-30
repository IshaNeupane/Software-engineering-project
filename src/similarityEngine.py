class SimilarityEngine:
    def __init__(self, threshold: float = 0.7):
        self.threshold = threshold

    def calculateSimilarity(self, a1, a2):
        """
        Simple similarity: compares content strings and returns how similar they are.
        """

        if not a1.content or not a2.content:
            return 0.0

        text1 = a1.content
        text2 = a2.content

        # Convert both texts to lowercase to ignore capitalization differences
        text1 = text1.lower()
        text2 = text2.lower()

        # Count matching characters in the same positions
        min_len = min(len(text1), len(text2))
        match_count = 0

        for i in range(min_len):
            if text1[i] == text2[i]:
                match_count += 1

        # Similarity score = matched characters / shortest text length
        return match_count / min_len
    