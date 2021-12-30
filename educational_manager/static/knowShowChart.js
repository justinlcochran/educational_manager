function add_item(elem) {
    const category = `${elem.name}-div`
    console.log(category)
    const c = document.getElementById(`${category}`).childElementCount;
    const option = document.createElement('textarea')
            option.setAttribute('type', 'textfield')
            option.setAttribute('class', 'center')
            option.setAttribute('id', `${elem.name}${c+1}`)
            option.setAttribute('name', `${elem.name}${c+1}`)
            option.setAttribute('form', 'chartBuilder')
            option.setAttribute('onkeyup', "if (this.scrollHeight > this.clientHeight) this.style.height = this.scrollHeight + 'px';")
            document.getElementById(`${category}`).appendChild(option)
}

function standardContentDisplay() {
    let x = document.getElementById("standardsDropDown").value;
    let text = document.getElementById(x).textContent;
    document.getElementById('display-text').textContent = text;
}

function popupDisplay(pk) {
    var popup = document.getElementById(pk);
    popup.classList.toggle("show");
}