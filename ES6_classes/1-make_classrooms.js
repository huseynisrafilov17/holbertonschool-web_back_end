import ClassRoom from "./0-classroom.js";

export default function initializeRooms() {
  let object1 = new ClassRoom(19);
  let object2 = new ClassRoom(20);
  let object3 = new ClassRoom(34);
  return [object1, object2, object3]
}
