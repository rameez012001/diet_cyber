$(document).ready(()=>{
    var feedback=(color,result,x,y)=>{
        $('#result').css('color',color);
        $('#result').text(result);
        $('#feedback').text(x);
        $('#feedback').css('color',color);
        let z = 21.7*y; 
        $('#result1').text(z.toFixed(1));
    }
    $('#bmi').click(()=>{
        let height = $('#height').val();
        let weight = $('#weight').val();
        let metre = height/100; 
        // bmi calculations
        let m2 = metre*metre;
        let bmi = weight/m2;
        let rbmi = bmi.toFixed(1);
           
        if(height.value==""||weight.value==""){
            feedback('black',"NaN",'Invalid',m2)
        }
        else{
            if(rbmi<18.5){
                feedback('orange',rbmi,'Underweight',m2)
            }else if(rbmi>=18.5&&rbmi<=24.9){
                feedback('green',rbmi,'Normal',m2)                
            }else if(rbmi>=25&&rbmi<=29.9){
                feedback('red',rbmi,'Overweight',m2)
            }else if(bmi>30){
                feedback('darkred',rbmi,'Obese',m2)
            }else{
                feedback('black',"NaN",'Invalid',m2)
            }
        }
    });
    let pro = ()=>{
        let a =2000;
        let b =$('#caltot').text();
        let c = b/a;
        let d = c*100;
        $('#progress2').css({"width":d+"%",'transition': 'width 3s'});
        (b>100)?
        $('#num').text(b):false;
        

        anychart.onDocumentReady(()=> {
            let cal =$('#caltot').text();
            let pro =$('#calpro').text();
            let fat =$('#calfat').text();
            var data = [
                {x: "Calories", value:cal},
                {x: "Protein", value:pro},
                {x: "Fat", value:fat},
            ];
            var chart = anychart.pie();
            chart.title("Nutrition");
            chart.data(data);
            chart.container('piechart');
            chart.draw();
        });
    }
    pro();
});