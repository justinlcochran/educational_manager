function standardContentDisplay() {
    let x = document.getElementById("standardsDropDown").value;
    let text = document.getElementById(x).textContent;
    document.getElementById('display-text').textContent = text;

    $.ajax({
    type: 'GET',
    url: `/teacher/get_know_show/${x}`,
    success: function(response){
        let chartContainer = document.getElementById('chart-container')
        console.log(response.charts_query)
        const chartData = response.charts_query
        chartData.map(item=>{
            const option = document.createElement('div')
            option.textContent = item.standard
            option.setAttribute('class', 'item')
            option.setAttribute('id', item.id)
            chartContainer.appendChild(option)

            const knowShowCreator = item.creator
            const knowShowCreated = item.created
            const subOption = document.createElement('a')
            let link = `/teacher/instantiate_assessment/${item.id}`
            subOption.setAttribute('href', link)
            subOption.textContent = `${knowShowCreator}: ${knowShowCreated}`
            option.appendChild(subOption)

        })
    },
    error: function(error){
        console.log(error)
    }
})
}


