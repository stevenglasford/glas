//Code written by Steven Glasford
//Create a test file that is able to generate a sequence of dovetail fitting tests

tolerance=.13;
tq=19.05;
//Create a cube that will be cut

//generate a variety of tolerance sizes
//for (i = [1:8]){

//}



for(i=[1:8]){
    

    translate([0,0,(i-1)*(tq*3)]){
        //upper wing
        translate([0,tq-tq/2,tq*(2/3)]) cube([tq*2,tolerance*i,tq*(1/3)], true);
        translate([0,tq-tq/2,tq*(2/3)]) rotate([90+(90-78),180,180]) cube([tq*2,tolerance*i,tq*(1/3)],True);

//lower wing
        translate([0,tq-tq/2,0]) cube([tq*2,tolerance*i,tq*(1/3)],True);    
        translate([0,tq-tq/2,tq/3]) rotate([78,180,180]) cube([tq*2,tolerance*i,tq*(1/3)],True);
        

        
     cube([tq * 2,tq * 2,tq], True);
        
    }
}


