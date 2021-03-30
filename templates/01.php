<!DOCTYPE html>

<html lang="en">
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">
    <?php
        $title = "TEST";
            echo("<title>$title</title>");
        ?>
        
        <script>
       
            document.addEventListener('DOMContentLoaded', function() {

                let correct = document.querySelector('.correct');
                correct.addEventListener('click', function() {
                    correct.style.backgroundColor = 'green';
                    document.querySelector('#A1').innerHTML = 'Правильно';
            });

            let incorrects = document.querySelectorAll('.incorrect');
            for (let i = 0; i < incorrects.length; i++) {
                incorrects[i].addEventListener('click', function() {
                    incorrects[i].style.backgroundColor = 'red';
                    document.querySelector('#A1').innerHTML = 'Неправильно';

                });
            }
    
             document.querySelector('.check').addEventListener('click', function() {
                 let input = document.querySelector('input');
                 if (input.value === '17') {
                     input.style.backgroundColor = 'green';
                     document.querySelector('#A2').innerHTML = 'Правильно';
                 } else {
                     input.style.backgroundColor = 'red';
                     document.querySelector('#A2').innerHTML = 'Неправильно';
                 }
             });
           });
        </script>
    <style>

#A2, #A1 {color:rgba(60, 250, 234, 0.808);}

    p, h1, h3 {color:rgba(60, 250, 234, 0.808);}

    .center {
    margin: 0 auto;
    border-radius: 15px;
    padding: 1em 1em;
    font-family: 'Montserrat', sans-serif;
        background-image:
            linear-gradient(
            to right,
            rgba(39, 39, 39, 0.835), 
            rgba(1, 77, 100, 0.918)
); 
}

    button, input[type="submit"] {
    background-color: #d9edff;
    border: 1px solid transparent;
    border-radius: 0.15rem;
    font-size: 1.4rem;
    line-height: 1.5;
    margin: 4px;
    text-align: center;
    transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    vertical-align: middle;
}

    input[type="text"] {
    line-height: 2.1;
    border-radius: 0.35rem;
  
}

    input[type="text"]:hover {
    border-radius: 0.35rem;
   
}

    </style>
    </head>
    <body>
    <div class="center">

        <?php
        $name = "TEST";
            echo("<h1>$name</h1>");
    
      
        ?>
           
        <section>
        
            <article>
                <hr>
                <h3>How many times can you subtract 6 from 30?</h3>
                <button class="incorrect">ДВА РАЗA</button>
                <button class="incorrect">ЧЕТЫРЕ РАЗA</button>
                <button class="incorrect">ТРИ РАЗA</button>
                <button class="incorrect">ШЕСТЬ РАЗ</button>
                <button class="correct">ПЯТЬ РАЗ</button>
                <p id="A1">Сколько раз вы можете вычесть 6 из 30?</p>
            </article>
        
            <article>
                <hr>
                <h3>What number should be subtracted from each of 50, 61, 92, 117 so that the numbers, so obtained in this order, are in proportion ?</h3>
                <input type="text"></input>
                <button class="check">Check</button>
                <p id="A2">Какое число нужно вычесть из 50, 61, 92, 117, чтобы числа, полученные в таком порядке, были пропорциональны?</p>
            </article>
        </section>
        
    </div>
    
    </body>
</html>
