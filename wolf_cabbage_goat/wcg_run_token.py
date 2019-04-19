import wcg_token
import depth_first_search_hash

wcg = wcg_token.WCG_Token()
for i in depth_first_search_hash.depth_first_search(wcg,wcg.start()):
    print(i)
