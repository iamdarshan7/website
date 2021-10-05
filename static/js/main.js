// for appliform 
const avitBox = document.getElementById('avit-box')

setTimeout(function(){ 
    avitBox.style.display = "none"; 
 }, 3000);





/* for form submission */



const alertBox = document.getElementById('alert-box')
const form = document.getElementById('p-form')


const f_name = document.getElementById('id_first_name')
const l_name = document.getElementById("id_last_name")
const email = document.getElementById('id_email')
const phone = document.getElementById('id_phone')
const college = document.getElementById('id_college')
const program = document.getElementById('id_program')
const files = document.getElementById("id_files")
// const percentage = document.getElementById('percentage-box')
// const percentageClick = document.getElementById('percentage')

// console.log(program)
// const csrf = document.getElementsByName('csrfmiddlewaretoken')
// console.log(csrf)


const handleAlerts = (type, text) => {
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
    ${text}
    </div>`
}

// program-data (not needed)
// programClick.addEventListener('mouseover', e => {
//     e.preventDefault()

//     $.ajax({
//         type: 'GET',
//         url: '/program-data/',
//         success: function(response){
//             console.log(response.data)
//             const proData = response.data
//             proData.map(item => {
//                 const option = document.createElement('div')
//                 option.textContent = item.title
//                 option.setAttribute('class', 'item')  
//                 option.setAttribute('data-value', item.title)
//                 program.appendChild(option)

//             })
//         },
//         error: function(error){
//             console.log(error)
//         }
//     })
// })

// percentage-data (not needed)
// percentageClick.addEventListener('mouseover', e => {
//     e.preventDefault()

//     $.ajax({
//         type: 'GET',
//         url: '/percentage-data/',
//         success: function(response){
//             console.log(response.data)
//             const perData = response.data
//             perData.map(item => {
//                 const option = document.createElement('div')
//                 option.textContent = item.title
//                 option.setAttribute('class', 'item') 
//                 option.setAttribute('data-value', item.title)
//                 percentage.appendChild(option)

//             })
//         },
//         error: function(error){
//             console.log(error)
//         }
//     })
// })


// Elements for program and percentage (not needed )
// const text_Program = document.getElementById('id_program')
// const text_Percentage = document.getElementById('id_percentage')



// after submitting data
form.addEventListener('submit', e => {
    e.preventDefault()

    const fd = new ApplicationFormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('first_name', f_name.value)
    fd.append("last_name",l_name.value)
    fd.append('email', email.value)
    fd.append('phone', phone.value)
    fd.append('college', college.value)
    fd.append('program', program.value)
    fd.append("files", files.value)



    $.ajax({
        // url: "{% url 'AppFormDetail' %}",
        type: "POST",
        enctype: 'multipart/form-data',
        data: fd,
        success: function (response) {
            console.log(response)
            const sText = `<div>
            <h4>OKAY</h4>
            <p>With your educational background, 
            you can apply for further studies.</p>
        </div>`
            handleAlerts('success', sText)
            setTimeout(() => {
                alertBox.innerHTML = ''
                f_name.value = ''
                l_name.value = ""
                email.value = ''
                phone.value = ''
                college.value = ""
                program.value = ""


            }, 3000)
            // form.classList.add('hidden')
            // document.getElementById('another_form').classList.remove('hidden')
        
    },
        error : function (error) {
            console.log(error)
            handleAlerts('danger', 'oops..something went wrong')
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})



console.log(form)

// (not needed)
// document.getElementById('p-form').classList.add('hidden')
// document.getElementById('another_form').classList.remove('hidden')