var array1 = [
    ["2302 W 14th St", "Wilmington", "DE", "19806", "New Castle", "DENC508522", "342300","$358,000","75","12/29/2020", "Wilm #13", "Red Clay Consolidated", "0.09", "FreeSimple", "No", "No", "No", "N/A","N/A", "1925","1650", "4","2","2","0","1","Three","Colonial,Traditional", "Yes", "Carpet,CeramicTile,Hardwood","NaturalGas", "Public","PublicSewer", "Yes", "Full,Unfinished","Brick","Asphalt,Shingle","No","WindowUnits","NaturalGas","377705","$360,634.79","More than 2 months", "Unknown"]
]

function display_arrayListPrice()
{
    e =array1[0][7];
    


   document.getElementById("Result").innerHTML = e;
   
}
function display_arrayExpectedPrice()
{
    e =array1[0][41];
    document.getElementById("expectedListPrice").innerHTML = e;
}

function display_arrayDaysOnMarket()
{
    e =array1[0][42];
    document.getElementById("Result").innerHTML = e + " days";
}

var array = [
    [ "$342,300","$358,000","Unknown","75","12/29/2020","New Castle","DENC508522", "Wilm #13", "Red Clay Consolidated", "0.09", "FreeSimple", "No", "No", "No", "N/A","N/A", "1925","1650", "4","2","2","0","1","Three","Colonial,Traditional", "Yes", "Carpet,CeramicTile,Hardwood","NaturalGas", "Public","PublicSewer", "Yes", "Full,Unfinished","Brick","Asphalt,Shingle","No","WindowUnits","NaturalGas","377705","360634.79","More than 2 months", "Unknown"]
]

function display_arrayYourHome()
{
  e0 = array[0][0];e1=array[0][1];e2 = array[0][2];e3=array[0][3];e4 = array[0][4];e5=array[0][5];e6 = array[0][6];e7=array[0][7];e8 = array[0][8];e9=array[0][9];e10 = array[0][10];e11=array[0][11];e12 = array[0][12];e13=array[0][13];e14 = array[0][14];e15=array[0][15];
  e16 = array[0][16];e17=array[0][17];e18 = array[0][18];e19=array[0][19];e20 = array[0][20];e21=array[0][21];e22 = array[0][22];e23=array[0][23];e24= array[0][24];e25=array[0][25];e26 = array[0][26];e27=array[0][27];e28 = array[0][28];e29=array[0][29];e30 = array[0][30];
  e32=array[0][32];e33=array[0][33];e34=array[0][34];e35=array[0][35];e36=array[0][36];e37=array[0][37];e38=array[0][38];e39=array[0][39];e40=array[0][40];
  document.getElementById("e0").innerHTML = e0;document.getElementById("e1").innerHTML = e1;  document.getElementById("e2").innerHTML = e2;document.getElementById("e3").innerHTML = e3;
  document.getElementById("e4").innerHTML = e4;  document.getElementById("e5").innerHTML = e5;  document.getElementById("e6").innerHTML = e6;  document.getElementById("e7").innerHTML = e7;
  document.getElementById("e8").innerHTML = e8;  document.getElementById("e9").innerHTML = e9;  document.getElementById("e10").innerHTML = e10;  document.getElementById("e11").innerHTML = e11;
  document.getElementById("e12").innerHTML = e12;  document.getElementById("e13").innerHTML = e13;  document.getElementById("e14").innerHTML = e14;  document.getElementById("e15").innerHTML = e15;
  document.getElementById("e16").innerHTML = e16;  document.getElementById("e17").innerHTML = e17;  document.getElementById("e18").innerHTML = e18;  document.getElementById("e19").innerHTML = e19;
  document.getElementById("e20").innerHTML = e20;  document.getElementById("e21").innerHTML = e21;  document.getElementById("e22").innerHTML = e22;  document.getElementById("e23").innerHTML = e23;
  document.getElementById("e24").innerHTML = e24;  document.getElementById("e25").innerHTML = e25;  document.getElementById("e26").innerHTML = e26;  document.getElementById("e27").innerHTML = e27;
  document.getElementById("e28").innerHTML = e28;  document.getElementById("e29").innerHTML = e29;  document.getElementById("e30").innerHTML = e30;  document.getElementById("e31").innerHTML = e31;
  document.getElementById("e32").innerHTML = e32;  document.getElementById("e33").innerHTML = e33;  document.getElementById("e34").innerHTML = e34;  document.getElementById("e35").innerHTML = e35;
  document.getElementById("e36").innerHTML = e36;  document.getElementById("e40").innerHTML = e40;

}
