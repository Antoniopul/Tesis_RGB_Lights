/*
  Código utilizado para el segundo incremento en el trabajo de tesis
*/
//EL SENSOR ULTRASONICO FUNCIONA A 5V
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
//LIBRERIA PARA CONTROLAR EL SENSOR ULTRASONICO
#include <NewPingESP8266.h>

//------------------------------------------[DEFINICION DE CLASES Y VARIABLES PARA LA CONEXION A WIFI Y MQTT]--------------------------------------------
// ACTUALIZAR CON LOS DATOS DE LA RED EN LA QUE SE ENCUNTRA EL BROKER MQTT
const char* ssid = "Red_MQTT";    //Red_MQTT
const char* password = "pruebatesis321";    //pruebatesis321
const char* mqtt_server = "192.168.16.230";    //192.168.253.230
WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
char msg_dis[MSG_BUFFER_SIZE];
int value = 0;
String msg_response;
String msg_distance_response;
//float distance;

//----------------------------------------[DEFINICION DE PINES PARA EL SENSOR ULTRASONICO CON LA LIBRERIA NEWPING]----------------------------------------
#define TRIGGER_PIN  2  // Arduino pin tied to trigger pin on the ultrasonic sensor. //D4
#define ECHO_PIN     0  // Arduino pin tied to echo pin on the ultrasonic sensor. //D3
#define MAX_DISTANCE 400 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.
NewPingESP8266 sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPingESP8266 setup of pins and maximum distance.
//-------------------------------------------------------[FUNCION PARA LA CONEXION DEL ESP8266 A WIFI]-----------------------------------------------------
void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  randomSeed(micros());
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

//--------------------------------------------[CREACION DEL LA DEVOLUCION DE LA POSLLAMADA PARA EL PROTOCOLO MQTT]------------------------------------------
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

//-------------------------------------------------------[FUNCION PARA LA RECONEXION CON EL BROKER MQTT]-----------------------------------------------------
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("electronica/cevada", "hello world reconncected");
      // ... and resubscribe
      client.subscribe("inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
//-------------------------------------------------------[FUNCION DE INICIO DE CONFIGURACIONES]-----------------------------------------------------
void setup() {
  Serial.begin(115200); // Starts the serial communication
  
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

}
//---------------------------------------------------------------------[FUNCION LOOP]----------------------------------------------------------------
void loop(){
  delay(100);      
  //int distance = sonar.ping_cm();
  int distance = sonar.ping_median(20);
  distance = sonar.convert_cm(distance);

  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  unsigned long now = millis(); //Envia los datos cada 1 segundos
  if (now - lastMsg > 1000) {
    lastMsg = now;
    ++value;

    if (distance >= 220 && distance <= 250) {
    msg_response = "Dentro del Rango en A1 - Distancia:" + String(distance);
    snprintf (msg, MSG_BUFFER_SIZE, msg_response.c_str(), value);
    client.publish("Tesis_ESP/Node1", msg);
  } else {
    msg_distance_response = "Distancia: " + String(distance);
    snprintf (msg_dis, MSG_BUFFER_SIZE, msg_distance_response.c_str(), value);
    client.publish("Tesis_ESP/Node1",msg_dis);
  }
  
  }
 }
