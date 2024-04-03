let addbtns = document.querySelectorAll(".add");
let table = document.querySelector("table");
let total = document.querySelector("b");
let itemlist = []
let row;

for(let i=0; i<addbtns.length; i++){
    let addbtn = addbtns[i];
    addbtn.addEventListener("click", ()=>{
        item = addbtn.parentElement.getElementsByTagName("h3")[0].innerText;
        if(itemlist.includes(item)){
            alert(item+" is already added to cart");
            return;
        }
        else{
            itemlist.push(item);
        }
        //create new row
        row = document.createElement("tr");
        table.appendChild(row);
        //name cell
        let name = document.createElement("td");
        row.appendChild(name);
        let nameinput = document.createElement("input");
        row.appendChild(nameinput);
        nameinput.type = "hidden";
        name.innerText = addbtn.parentElement.getElementsByTagName("h3")[0].innerText;
        nameinput.value = name.innerText;
        nameinput.name = "medicines";
        //dosage cell
        let dosage = document.createElement("td");
        row.appendChild(dosage);
        let dosageinput = document.createElement("input");
        dosage.append(dosageinput);
        dosageinput.type = "text";
        dosageinput.placeholder = "X-X-X-X";
        dosageinput.maxLength = 7;
        dosageinput.style.width = "70px";
        //quantity cell
        let quantity = document.createElement("td");
        row.appendChild(quantity);
        let quantityinput = document.createElement("input");
        quantity.append(quantityinput);
        quantityinput.type = "number";
        quantityinput.value = 1;
        quantityinput.min = 1;
        quantityinput.max = 8;
        //price cell
        let price = document.createElement("td");
        row.appendChild(price);
        price.innerText = addbtn.parentElement.getElementsByTagName("h4")[0].innerText;
        //add to cart total
        total.innerText = parseInt(total.innerText.replace('Rs.','')) + parseInt(price.innerText.replace('Rs.',''));
        //quantity change
        let before = 1;
        quantityinput.addEventListener("change", ()=>{
            let after = quantityinput.value;
            let priceint = addbtn.parentElement.getElementsByTagName("h4")[0].innerText;
            price.innerText = "Rs."+(priceint.replace('Rs.','') * quantityinput.value);
            if(before < after)
                total.innerText = parseInt(total.innerText.replace('Rs.','')) + parseInt(priceint.replace('Rs.',''));
            else
                total.innerText = parseInt(total.innerText.replace('Rs.','')) - parseInt(priceint.replace('Rs.',''));
            before = after;
        });
        //remove button
        let rmvbox = document.createElement("div");
        row.appendChild(rmvbox);
        rmvbox.setAttribute("id","rmvbox");
        let rmv = document.createElement("button");
        rmvbox.appendChild(rmv);
        rmv.innerText = "Remove";
        rmv.setAttribute("class","removebutton");
        rmv.addEventListener("click", (e)=>{
            table.removeChild(e.target.parentElement.parentElement);
            total.innerText = parseInt(total.innerText.replace('Rs.','')) - parseInt(e.target.parentElement.parentElement.childNodes[3].innerText.replace('Rs.',''));
            if(total.innerText == "NaN")
            total.innerText = "0";
            itemlist.pop(e.target.parentElement.parentElement.childNodes[0].innerText);
            if(table.childElementCount-1 > 0)
                generate.style.display = "block";
            else
                generate.style.display = "none";
        });
        //Generate Prescription Button
        let generate = document.querySelector("#generate");
        if(table.childElementCount-1 > 0)
            generate.style.display = "block";
        else
            generate.style.display = "none";
    });
};