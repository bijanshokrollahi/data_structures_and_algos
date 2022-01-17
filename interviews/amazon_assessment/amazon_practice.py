

class AmazonPractice:
    def searchSuggestions(self, repository: list, customerQuery: str) -> list:
        search_suggestions = []
        if len(customerQuery) < 2:
            return search_suggestions
        count = 0
        for i in range(0, len(customerQuery) - 1):
            search_suggestions.append([])
        for i in range(1, len(customerQuery)):
            curr_query = customerQuery[:i + 1].lower()
            if count == 0:
                for word in repository:
                    if curr_query in word.lower():
                        search_suggestions[i-1].append(word.lower())
            else:
                for word in search_suggestions[i-2]:
                    if curr_query in word.lower():
                        search_suggestions[i - 1].append(word.lower())
            count += 1
        for i in range(0, len(search_suggestions)):
            search_suggestions[i].sort()
            if len(search_suggestions[i]) > 3:
                search_suggestions[i] = search_suggestions[i][:3]
        return search_suggestions

    def amazon_fresh_winner(self, codeList, shoppingCart) -> int:
        import queue
        if len(codeList) == 0:
            return 1
        code_list_queue = queue.SimpleQueue()
        for group in codeList:
            for fruit in group:
                code_list_queue.put(fruit)
        i = 0
        while i < len(shoppingCart):
            code_item = code_list_queue.get()
            if code_item == 'anything' and shoppingCart[i] is not None:
                i += 1
            else:
                if shoppingCart[i] != code_item:
                    while shoppingCart[i] != code_item:
                        i += 1
                else:
                    i += 1
        return code_list_queue.qsize() == 0


