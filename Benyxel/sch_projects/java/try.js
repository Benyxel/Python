// let name_1 = "Kofi";
// let age_1 = 26
// let name_2 = "Kwame" ;
// let age_2 = 48

// if (age_1 > age_2) {
//     console.log(`${name_1} is older than ${name_2}`)
// }

// else {
//     console.log(`${name_2} is older than ${name_1}`)
// }


// age_1 > age_2 ? console.log(`${name_1} is older than ${name_2}`) : console.log(`${name_2} is older than ${name_1}`)

let data = ["Kwame", "Kofi", 43, 57, "Maame", "Abena", 45, 100]

for (let x of data){
    let ls = String(x);
    let als = ls.toLowerCase()
    if( als == "kofi"){
        console.log(x)
    }
    
}
    
    