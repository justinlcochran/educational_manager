function add_item(elem) {
    const table = document.getElementById('answers-table')
    const new_row = document.createElement('tr');
    new_row.setAttribute('id', `row${table.rows.length + 1}`)
    table.appendChild(new_row)
    const new_slot_1 = document.createElement('td')
    new_slot_1.setAttribute('id', `${new_row.id}-slot1`)
    new_row.appendChild(new_slot_1)
    const new_radio = document.createElement('input');
    new_radio.setAttribute('type', 'radio')
    new_radio.setAttribute('id', `answer${table.rows.length}-radio`)
    new_radio.setAttribute('name', `correct`)
    new_radio.setAttribute('value', `answer${table.rows.length}`)
    new_slot_1.appendChild(new_radio)
    const new_slot_2 = document.createElement('td')
    new_slot_1.setAttribute('id', `${new_row.id}-slot2`)
    new_row.appendChild(new_slot_2)
    const new_label = document.createElement('label')
    new_label.setAttribute('for', `answer${table.rows.length}-radio`)
    new_slot_2.appendChild(new_label)
    const new_textfield = document.createElement('textarea');
    new_textfield.setAttribute('type', 'textarea');
    new_textfield.setAttribute('class', 'center');
    new_textfield.setAttribute('id', `answer${table.rows.length}-text`);
    new_textfield.setAttribute('name', `answer${table.rows.length}-text`);
    new_textfield.setAttribute('form', 'assessmentBuilder');
    new_textfield.setAttribute('rows', '2');
    new_textfield.setAttribute('cols', '50');
    new_textfield.setAttribute('onkeyup', "if (this.scrollHeight > this.clientHeight) this.style.height = this.scrollHeight + 'px';");
    new_label.appendChild(new_textfield);
}
