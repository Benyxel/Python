function add() {
  
  const fn = document.querySelector("#fn").value;
  const sn = document.querySelector("#sn").value;
   let nfn = Number(fn);
    let nsn = Number(sn);
    let sum = nfn + nsn;
    
    document.querySelector("#text").innerHTML = sum
    
}
add()