import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let newUser;
  let newPhoto;
  try {
    newUser = await createUser();
    newPhoto = await uploadPhoto();
  } catch (e) {
    return {
      photo: null,
      user: null,
    };
  }
  return {
    photo: newPhoto,
    user: newUser,
  };
}
