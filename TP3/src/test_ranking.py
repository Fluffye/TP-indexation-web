from ranking import create_dict_ranking

TEST_QUERIES = [
    "chocolate",
    "chocolate box",
    "chocolate box usa",
    "dark chocolate with orange or any orange fruit really",
    "black chocolate box",
    "cute outfit",
    "black shoes",
    "shoes confortable for running",
    "energy drink",
    "blue energy dring",
]

WEIGHT_CONFIGS = {
    "baseline": [20, 30, 10, 5, 5, 3, 2],
    "more_title": [15, 30, 20, 5, 5, 3, 2],
    "more_reviews": [20, 20, 10, 5, 10, 5, 5],
    "bm25_focus": [30, 10, 10, 5, 5, 3, 2],
}

def test_queries(queries, weights, top_k=5):
    results = {}

    for query in queries:
        ranking_result = create_dict_ranking(query, weights)["results"]  # ta fonction de ranking
        results[query] = ranking_result[:top_k]

    return results




def run_tests():
    all_results = {}

    for name, weights in WEIGHT_CONFIGS.items():
        print(f"\n=== Testing configuration: {name} ===")
        results = test_queries(TEST_QUERIES, weights)

        all_results[name] = results

        for query, docs in results.items():
            print(f"\nQuery: {query}")
            for d in docs:
                print(d)

    return all_results

run_tests()
