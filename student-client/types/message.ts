export default interface Message {
  text: string;
  containsMath?: boolean;
  fromUser: boolean;
}
