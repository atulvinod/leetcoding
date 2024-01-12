const puzzle_input = require('./puzzle_input');

const test = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
,"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
,"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
,"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
,"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

const constraints = {
    'blue':14,
    'red':12,
    'green':13
}

function getGameId(input){
    const [game_id_part,] = input.split(':');
    const [,id_part] = game_id_part.split(' ')
    return Number(id_part);  
}

function getGameTurns(input){
    const [, game_part] = input.split(':').map((x)=>x.trim())
    const individual_games = game_part.split(";").map((s)=>s.trim());
    const formatted_games = individual_games.reduce((agg, v)=>{
       const game = {}
       const play = v.split(',').map((x)=>x.trim())
       play.forEach((p)=>{
        const [count, color] = p.split(' ')
        game[color] = count;
       }) 
       agg.push(game);
       return agg;
    },[])

    return formatted_games;
}

function isValidGame(games){
    for(let i = 0 ; i < games.length ; i++){
        let game = games[i]
        const entries = Object.entries(game);
        for(const [color, count] of entries){
            if(Number(count) > constraints[color]){
                return false;
            }
        }
    }

    return true;
}

function getMinCubesReqForAllGames(games){
    let result = {};
    games.forEach((game) => {
        const entries = Object.entries(game);
        for(const [color, count] of entries){
            result[color] = Math.max(result[color] ?? 0 , count);
        }
    })
    const cubes_counts = Object.values(result);
    const power_count = cubes_counts.reduce((agg, v)=>agg*v,1);
    return power_count;
}


function solvePart1(puzzle){
    let totalGames = 0;
    puzzle.forEach((input)=>{
        let id = getGameId(input);
        let game = getGameTurns(input);
        // console.log('game ',id)
        if(isValidGame(game)){
            // console.log('Possible game ',id)
            totalGames += id;
        }else{
            // console.log('Impossible game',id)
        }
    })

    console.log(totalGames)
}

function solvePart2(puzzle){
    let sumPowerSet = 0
    puzzle.forEach((input)=>{
        let game = getGameTurns(input);
        const cube_count = getMinCubesReqForAllGames(game);
        sumPowerSet += cube_count;
    })
    console.log(sumPowerSet);
}

// solvePart1(puzzle_input)
solvePart2(puzzle_input);