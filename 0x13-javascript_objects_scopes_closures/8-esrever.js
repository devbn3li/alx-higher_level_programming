exports.esrever = function (list) {
  const reversLs = [];

  for (let x = list.length - 1; x >= 0; x--) {
    reversLs.push(list[x]);
  }

  return reversLs;
};
