def unliharflar(words:str):
    unlilar=["aeuioAEUIO"]
    count=sum(word for word in words if word.isalpha() if word in unlilar)
    c1=sum(word for word in words if word.isalpha() if word not in unlilar)
    let={"Unlilar": count,"Undoshlar":c1}
    print(let)