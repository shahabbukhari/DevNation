// !Add Todo Item
const inputText = document.querySelector('.todo-input-text')
let locationEle = document.querySelector('.todo-list')
let addButton = document.querySelector('.todo-add')
let allTodos = []

inputText.addEventListener("keyup", addEle);
addButton.addEventListener('click', addEle)

function addEle(event) {
    let InputValue = inputText.value
    // FirstCondition: Check if enter key or add button is presses and it does'nt have only spaces
    const FirstCondition = (event.keyCode === 13 || event.target.classList[0] == 'fas') && InputValue.replace(/\s/g, '').length

    if (FirstCondition) {
        // SecondCondition: Check the value is not repeated
        let secondCondition;
        if (!allTodos.length) {
            secondCondition = true
        } else {
            secondCondition = allTodos.every( (e) => e['todo'] != InputValue)
        }

        if(secondCondition) {
            // Set Todo To todo Array
            setAllTodos(InputValue)
            localStorage.setItem('todos',JSON.stringify(allTodos));
            counter(+1)
            renderElements(InputValue)   
            inputText.value = ""
        }
}
}
function renderElements(val,chc=false,isCount = true) {
    // Create Todo Div
    const todoDiv = document.createElement('div')
    todoDiv.classList.add('todo')
    
    const content = innerContent(val,chc,isCount)
    todoDiv.appendChild(content[0])
    todoDiv.appendChild(content[1])
    
    locationEle.appendChild(todoDiv)
}
function innerContent(cont,chc=false,isCount) {
    let mainDiv = document.createElement('div')
    let myCheckbox = document.createElement('INPUT')
    let para = document.createElement('p')
    let innerImg = document.createElement('img')
    
    mainDiv.classList.add('todo-content')
    myCheckbox.classList.add('todo-checkbox')
    para.classList.add('todo-text')
    innerImg.classList.add('delete-todo')
    // console.log(chc);

    myCheckbox.setAttribute("type", "checkbox");
    para.innerText = cont
    innerImg.setAttribute('src', "images/icon-cross.svg")
    myCheckbox.checked = chc
    
    if(chc && isCount) counter(-1)

    mainDiv.appendChild(myCheckbox)
    mainDiv.appendChild(para)
    
    innerImg.addEventListener('click', deleteEle)
    myCheckbox.addEventListener('change', checkBoxHan)
    return [mainDiv, innerImg]
    // return (`
    //         <div class="todo-content">
    //         <input type="checkbox" class="todo-checkbox">
    //             <p class="todo-text">${cont}</p>
    //         </div>           
    //         <img src="images/icon-cross.svg" class="delete-todo">
    // `
    // )
}


// !Theme Changer
const theme = document.querySelector('.todo-mode')

theme.addEventListener('click', () => {
    document.body.classList.toggle('light-theme')
    document.body.classList.toggle('dark-theme')
    const themeSrc = theme.querySelector('.theme-img').src

    if (themeSrc.includes("moon")) {
        theme.querySelector('.theme-img').src = "images/icon-sun.svg" 
       document.querySelector('.bg-scene').src = "images/bg-desktop-dark.jpg"
    } else if (themeSrc.includes("sun")) {
       theme.querySelector('.theme-img').src = "images/icon-moon.svg" 
       document.querySelector('.bg-scene').src = "images/bg-desktop-light.jpg"
    }
})

// !Delete Element
function deleteEle(e) {
    locationEle.removeChild(this.parentNode)
    
    let currentValue = this.previousSibling.children[1].innerText
    for (todo of allTodos) {
        if (todo['todo'] == currentValue) {
            allTodos.splice(allTodos.indexOf(todo), 1)
        }
    }
    counter(-1)    
    localStorage.setItem('todos',JSON.stringify(allTodos));
}

// !CheckBox
function checkBoxHan(e) {
    let currentValue = this.nextSibling.innerHTML
    if(this.checked) {
        for (todo of allTodos) {
            if (todo['todo'] == currentValue) {
                todo['isChecked'] = true
                counter(-1)
            }
        }
    } else {
        for (todo of allTodos) {
            if (todo['todo'] == currentValue) {
                todo['isChecked'] = false
                counter(1)
            }
        }
    }

    localStorage.setItem('todos',JSON.stringify(allTodos));
}

// !set to local storage
function setAllTodos(val,chc=false) {
    allTodos.push({'todo':val,'isChecked': chc})
}

// !DOM LOAD EVENT 
window.addEventListener('DOMContentLoaded', () => {
    let fromLocal = localStorage.getItem('todos')
    if (fromLocal != null) {
        allTodos = JSON.parse(fromLocal)
    }
    if (allTodos != [] || allTodos != null) {
        allTodos.forEach( (todo) => {
            renderElements(todo['todo'],todo['isChecked'])
            counter(+1)
        })
    } 
})

// !.todos-left-counter 
function counter(num) {
    let left_counter_val = document.querySelector('.todo-left-counter')
    left_counter_val.innerText = parseInt(left_counter_val.innerText)+num    
}

// !Clear completed todos
const clearCompleted = document.querySelector('.clear-todo')
clearCompleted.addEventListener('click', (e) => {
    let nonCompleted = allTodos.filter( (todo) => todo["isChecked"] != true )
    locationEle.innerHTML = " "
    nonCompleted.forEach(todo => {
        renderElements(todo['todo'],todo['isChecked'])
    })
    allTodos = nonCompleted
    localStorage.setItem('todos', JSON.stringify(allTodos))
})

// !add Filtering logic
// ?Completed Todos
const completedBtn = document.querySelector('.todo-completed-filter')
completedBtn.addEventListener('click', () => {
    filter(true)
})
// ?Active Todos
const activeBtn = document.querySelector('.todo-active-filter')
activeBtn.addEventListener('click', () => {
    filter(false)
})
// ?all Todos
const allBtn = document.querySelector('.todo-all-filter')
allBtn.addEventListener('click', () => {
    filter('all')
})

function filter(isChecked) {
    let filtered;
    if (isChecked == true || isChecked == false) {
        filtered = allTodos.filter( (todo) => todo["isChecked"] == isChecked )
    } else {
        filtered = allTodos
    }
    console.log('worked');
    locationEle.innerHTML = " "
    filtered.forEach(todo => {
        renderElements(todo['todo'],todo['isChecked'],false)
    })
}