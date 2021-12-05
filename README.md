## StratoFlight-Camera

### Test-System
| Name 							| Usage |
| ---      						| --- |
| Raspberry Pi Model 3B+   		| Power source, taking pictures & sending I2C commands |
| Raspberry Pi NoIR Camera V2.1	| Taking pictures with different settings |
| PWM-PCB with PCA9865			| Creating a PWM-signal over I2C to turn servo motor |
| Micro Servo 9g (DF9GMS) 		| Turning the camera around the z-axis |

#### Raspberry Pi Used Pinout
| Pin # | Name 			| Usage								|
| --- 	| --- 			| --- 								|
| 04 	| 5V DC-Power 	| Power for servo motor and PCA9685	|
| 03 	| SDA1 (I2C) 	| SDA for I2C network				|
| 05 	| SCL1 (I2C) 	| SCL for I2C network				|
| 39 	| Ground 		| GND								|

***

### Flying-System
| Name 							| Usage |
| ---      						| --- |
| Raspberry Pi Zero   			| Power source, taking pictures & sending I2C commands |
| Raspberry Pi NoIR Camera V2.1	| Taking pictures with different settings |
| PWM-PCB with PCA9865			| Creating a PWM-signal over I2C to turn servo motor |
| Micro Servo 9g (DF9GMS) 		| Turning the camera around the z-axis |

***

### PWM-PCB
The PWM-PCB is a simple circuit board which can handle two PWM outputs using the PCA9685 I2C IC to simplify the needed code and take some load off the Pi Zero. One output is then used to set the turning angle of the SER0006 (DF9GMS) servo motor. The other output is not (yet) used.

![PCB for PWM](./pictures/PWM-PCB.png "PWM-PCB")
