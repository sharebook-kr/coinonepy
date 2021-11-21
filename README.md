# coinonepy
python wrapper for coinone 

# Public API
## 현재가 조회

```
import coinonepy

xrp_price = coinonepy.get_current_price("xrp")
print(xrp_price)
```

```
import coinonepy

price = coinonepy.get_current_price("xrp", verbose=True)
print(price)
```
