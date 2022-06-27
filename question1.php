<?php
interface action{

    public function energy();
    public function drive();
    public function fast();
    public function slow();

}

// 使用interface需依照規範，將介面所定義的方法時做出來，此時需使用到implements做實現
class Transportation implements action{


    public $label = '';
    public $engine = '';
    public $seats = '';
    public $color = '';

    function __construct($label, $engine, $seats, $color){
        $this->label = $label;
        $this->engine = $engine;
        $this->seats = $seats;
        $this->color = $color;
    }

    function showInfo(){
        echo $this->label;
        echo $this->engine;
        echo $this->seats;
        echo $this->color;
    }

    function energy(){
        $this->oil();
        $this->elec();
    }

    function drive(){
        $this->fast();
        $this->slow();
    }
    function fast(){
        
    }
    function slow(){
        
    }
    function oil(){

    }
    function elec(){

    }

}

// 子類別
class Car extends Transportation{

    function fast() {
        echo '加速中';
    }

    function elec() {
        echo '使用電力';
    }
}

// 子類別
class Moto extends Transportation{

    function slow() {
        echo '減速中';
    }

    function oil() {
        echo '使用汽油';
    }
}


// 透過Transportation作為交通工具大項目來延伸後續的『汽車』&『機車』類別
$car = new Car('Toyota', '2000cc', '4', 'white');
$car->showInfo();
echo '<br>';
$car->drive();
echo '<br>';
$car->energy();
echo '<br>';

$moto = new Moto('Kawasaki', '650cc', '2', 'green');
$moto->showInfo();
echo '<br>';
$moto->drive();
echo '<br>';
$moto->energy();
echo '<br>';
