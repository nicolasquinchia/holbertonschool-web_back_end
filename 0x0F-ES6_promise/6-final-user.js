import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const finalUser = await signUpUser(firstName, lastName);
  let finalPhoto;
  try {
    finalPhoto = await uploadPhoto(fileName);
  } catch (e) {
    finalPhoto = e.toString();
  }
  return [
    { value: finalUser, status: 'fulfilled' },
    { value: finalPhoto, status: 'rejected' },
  ];
}
