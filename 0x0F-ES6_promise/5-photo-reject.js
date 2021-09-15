export default function uploadPhoto(filename) {
  const myPromise = Promise.reject(
    new Error(`${filename} cannot be processed`),
  );
  return myPromise;
}
