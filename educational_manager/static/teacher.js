const standardSpace = document.getElementById('standardSpace')

$.ajax({
    type: 'GET',
    url: '/teacher/get_standards/',
    success: function(response){
        console.log(response.standard_list)
        const standardData = response.standard_list
        standardData.map(item=>{
            const option = document.createElement('div')
            option.textContent = item.code
            option.setAttribute('class', 'item')
            option.setAttribute('id', item.code)
            standardSpace.appendChild(option)

            const standardText = item.text
            const subOption = document.createElement('p')
            subOption.textContent = item.text
            option.appendChild(subOption)

        })
    },
    error: function(error){
        console.log(error)
    }
})

