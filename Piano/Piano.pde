import processing.sound.*;

SoundFile C4;
SoundFile D4;
SoundFile E4;
SoundFile F4;
SoundFile G4;
SoundFile A4;
SoundFile B4;
SoundFile C5;


void setup() {
  size(600, 600);

  C4 = new SoundFile(this, "Assets/Piano.mf.C4.aiff");
  D4 = new SoundFile(this, "Assets/Piano.mf.D4.aiff");
  E4 = new SoundFile(this, "Assets/Piano.mf.E4.aiff");
  F4 = new SoundFile(this, "Assets/Piano.mf.F4.aiff");
  G4 = new SoundFile(this, "Assets/Piano.mf.G4.aiff");
  A4 = new SoundFile(this, "Assets/Piano.mf.A4.aiff");
  B4 = new SoundFile(this, "Assets/Piano.mf.B4.aiff");
  C5 = new SoundFile(this, "Assets/Piano.mf.C5.aiff");
}

void draw() {
}


void keyPressed() {
  if (key == 'a') {
    C4.play();
  }
  if (key == 's') {
    D4.play();
  }
  if (key == 'd') {
    E4.play();
  }
  if (key == 'f') {
    F4.play();
  }
  if (key == 'g') {
    G4.play();
  }
  if (key == 'h') {
    A4.play();
  }
  if (key == 'j') {
    B4.play();
  }
  if (key == 'k') {
    C5.play();
  }
}
