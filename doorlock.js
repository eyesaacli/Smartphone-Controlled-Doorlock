#!/usr/bin/env node

// determines the number of degrees that the servo twists
// here, this creates roughly 90 degrees of rotation
var unlockedState = 500; // in microseconds, equivalent to 0.5ms pulse width
var lockedState = 1500; // in microseconds, equivalent to 1.5ms pulse width

var motorPin = 14; // Gpio Pin to which the servo's signal wire is connected to

var blynkToken = 'blynk_token_here'; // Blynk Token sent from app, each person's is different

//Setup servo
var Gpio = require('pigpio').Gpio; //requiring the pigpio module
var motor = new Gpio(motorPin, {mode: Gpio.OUTPUT}); // setting the motor as output

//Setup blynk
var Blynk = require('blynk-library'); //requiring the blynk-library module
var blynk = new Blynk.Blynk(blynkToken);
var v0 = new blynk.VirtualPin(0);

console.log("locking door")
lockDoor()

v0.on('write', function(param) {
	console.log('V0:', param);
  	if (param[0] === '0') { //unlocked
  		unlockDoor()
  	} else if (param[0] === '1') { //locked
  		lockDoor()
  	} else {
  		blynk.notify("Door lock button was pressed with unknown parameter");
  	}
});

blynk.on('connect', function() { console.log("Blynk ready."); });
blynk.on('disconnect', function() { console.log("DISCONNECT"); });

function lockDoor() {
	motor.servoWrite(lockedState);
  	
  	//After 1.5 seconds, the door lock servo turns off to avoid stall current
  	setTimeout(function(){motor.servoWrite(0)}, 1500)
}

function unlockDoor() {
	motor.servoWrite(unlockedState);
  	blynk.notify("Door has been unlocked!"); 

  	//After 1.5 seconds, the door lock servo turns off to avoid stall current
  	setTimeout(function(){motor.servoWrite(0)}, 1500)
}