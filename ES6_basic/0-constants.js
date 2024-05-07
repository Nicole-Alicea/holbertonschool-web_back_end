export function taskFirst():string {
    const task = 'I prefer const when I can.';
    return task;
}

export function getLast():string {
    return ' is okay';
}

export function taskNext():string {
    let combination = 'But sometimes let';
    combination += getLast();

    return combination;
}
