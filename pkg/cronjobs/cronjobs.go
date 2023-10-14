package cronjobs

import (
	"github.com/robfig/cron/v3"
	"github.com/seriousm4x/wubbl0rz-archiv-backend/pkg/logger"
)

var twitchDownloadsRunning bool

func init() {
	c := cron.New()

	logger.Debug.Println("[cronjob] registering job: emote update")
	if _, err := c.AddFunc("@every 1h", UpdateEmotes); err != nil {
		logger.Error.Println(err)
	}

	logger.Debug.Println("[cronjob] registering job: stream status")
	if _, err := c.AddFunc("@every 1m", SetStreamStatus); err != nil {
		logger.Error.Println(err)
	}

	logger.Debug.Println("[cronjob] registering job: twitch downloads")
	if _, err := c.AddFunc("@every 1h", RunTwitchDownloads); err != nil {
		logger.Error.Println(err)
	}

	logger.Debug.Printf("[cronjob] registered %d jobs", len(c.Entries()))

	logger.Debug.Println("[cronjob] inital run for all jobs")
	for _, job := range c.Entries() {
		job.Job.Run()
	}

	c.Start()
}

func RunTwitchDownloads() {
	if twitchDownloadsRunning {
		return
	}

	// run downloads
	twitchDownloadsRunning = true
	downloaded_items := 0

	count, err := DownloadVods()
	if err != nil {
		logger.Error.Println(err)
	}
	downloaded_items += count

	count, err = DownloadClips()
	if err != nil {
		logger.Error.Println(err)
	}
	downloaded_items += count

	if err := DownloadGames(); err != nil {
		logger.Error.Println(err)
	}

	twitchDownloadsRunning = false
}
