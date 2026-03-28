def generate_reasoning(status, buzz, evidence, rag_result):
    if rag_result:
        return "This brand is officially recognized with sustainability certification."
    if evidence:
        return "The product provides material-based or measurable sustainability details."
    if buzz:
        return "The product relies on vague sustainability buzzwords without proof."
    return "Not enough sustainability-related information found."