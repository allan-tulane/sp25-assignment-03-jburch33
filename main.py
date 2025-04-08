test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if S == "":
        return len(T)
    elif T == "":
        return len(S)
    elif S[0] == T[0]: ## a match
        return MED(S[1:], T[1:])
    else:
        insert = MED(S, T[1:]) ## insert a character
        delete = MED(S[1:], T) ## delete a character
        substitute = MED(S[1:], T[1:]) ## substitute a character
        return 1 + min(insert, delete, substitute) ## return the minimum cost


def fast_MED(S, T, memo=None):
    if memo is None: 
        memo = {}
    if (S, T) in memo: 
        return memo[(S, T)] 
    if S == "": ## base case
        memo[(S, T)] = len(T) 
    elif T == "": ## base case
        memo[(S, T)] = len(S) ## return the length of the string
    elif S[0] == T[0]: ## a match
        memo[(S, T)] = fast_MED(S[1:], T[1:], memo) ## return the minimum cost
    else: ## a mismatch insert, delete, or substitute
        insert = fast_MED(S, T[1:], memo) 
        delete = fast_MED(S[1:], T, memo)
        substitute = fast_MED(S[1:], T[1:], memo)
        memo[(S, T)] = 1 + min(insert, delete, substitute) ## return the minimum cost
    return memo[(S, T)]


def fast_align_MED(S, T, align_memo=None, cost_memo=None): ## memoization
    if align_memo is None: 
        align_memo = {}
    if cost_memo is None:
        cost_memo = {}

    if (S, T) in align_memo: ## if the alignment is already in the memo
        return align_memo[(S, T)] ## return the alignment

    if S == "": ## base case
        return "-" * len(T), T ## return the alignment
    if T == "": ## base case
        return S, "-" * len(S)     ## return the alignment

    if S[0] == T[0]: ## a match
        align_S, align_T = fast_align_MED(S[1:], T[1:], align_memo, cost_memo) 
        result = (S[0] + align_S, T[0] + align_T) 
    else: ## a mismatch
        insert_cost = fast_MED(S, T[1:], cost_memo)  
        delete_cost = fast_MED(S[1:], T, cost_memo) 
        substitute_cost = fast_MED(S[1:], T[1:], cost_memo) 

        min_cost = min(insert_cost, delete_cost, substitute_cost) ##  the minimum cost

        if min_cost == substitute_cost: ## if the minimum cost is the substitute cost
            align_S, align_T = fast_align_MED(S[1:], T[1:], align_memo, cost_memo) 
            result = (S[0] + align_S, T[0] + align_T)     ## return the alignment
        elif min_cost == insert_cost: ## if the minimum cost is the insert cost
            align_S, align_T = fast_align_MED(S, T[1:], align_memo, cost_memo) 
            result = ("-" + align_S, T[0] + align_T) 
        else: ## if the minimum cost is the delete cost
            align_S, align_T = fast_align_MED(S[1:], T, align_memo, cost_memo)
            result = (S[0] + align_S, "-" + align_T) 

    align_memo[(S, T)] = result ## store the alignment in the memo
    return result 
